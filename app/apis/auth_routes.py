from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, timedelta
import sqlite3
import hashlib
from passlib.context import CryptContext
from app.database.db_core import get_db_connection
from app.authentication.auth import create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

router = APIRouter(prefix="/auth", tags=["authentication"])
security = HTTPBearer()
# Argon2 is more secure, handles passwords of any length, and is OWASP recommended
# Keep bcrypt schemes for backward compatibility with existing hashes
pwd_context = CryptContext(
    schemes=["argon2", "bcrypt_sha256", "bcrypt"], 
    deprecated="auto",
    argon2__memory_cost=65536,  # 64 MB memory cost
    argon2__time_cost=3,        # 3 iterations
    argon2__parallelism=4       # 4 parallel threads
)

# Utility functions
def hash_password(password: str) -> str:
    """Hash password using Argon2 (handles passwords of any length, more secure than bcrypt)."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password, supporting Argon2 (new), bcrypt_sha256, and legacy bcrypt hashes."""
    try:
        if pwd_context.verify(plain_password, hashed_password):
            return True
    except (ValueError, Exception):
        # Handle any verification errors gracefully
        pass

    # Legacy fallback: hashes created before Argon2 rollout (manual SHA-256 + bcrypt)
    # This is for backward compatibility with old bcrypt hashes
    if hashed_password.startswith("$2"):  # bcrypt hash identifier
        sha256_hash = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
        try:
            return pwd_context.verify(sha256_hash, hashed_password)
        except (ValueError, Exception):
            return False
    
    return False

def get_password_hash(password: str) -> str:
    """Alias for hash_password for backward compatibility"""
    return hash_password(password)

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    phone_country_code: Optional[str] = "+1"
    date_of_birth: Optional[str] = None
    nationality: Optional[str] = None
    passport_number: Optional[str] = None
    passport_expiry_date: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    date_of_birth: Optional[str]
    nationality: Optional[str]
    passport_number: Optional[str]
    passport_expiry_date: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: datetime
    last_login: Optional[datetime]

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    phone_country_code: Optional[str] = None
    date_of_birth: Optional[str] = None
    nationality: Optional[str] = None
    passport_number: Optional[str] = None
    passport_expiry_date: Optional[str] = None

class PassengerCreate(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    date_of_birth: str
    passport_number: str
    passport_expiry_date: str
    passport_issuance_country: str
    nationality: str
    gender: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
    phone_country_code: Optional[str] = None

class PassengerUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    passport_number: Optional[str] = None
    passport_expiry_date: Optional[str] = None
    passport_issuance_country: Optional[str] = None
    nationality: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    phone_country_code: Optional[str] = None

class PassengerResponse(BaseModel):
    id: int
    user_id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    date_of_birth: str
    passport_number: str
    passport_expiry_date: str
    passport_issuance_country: str
    nationality: str
    gender: str
    email: Optional[str]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    created_at: datetime

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

# User management routes
@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    """Register a new user.
    
    Args:
        user (UserCreate): User registration data.
    
    Returns:
        UserResponse: Registered user data.

    Example:
    ```json
    {
        "email": "cenzer2@gmail.com",
        "password": "Apples@22",
        "first_name": "Sanjay",
        "middle_name": "Kumar",
        "last_name": "Patel",
        "phone_number": "6366555056",
        "phone_country_code": "+91",
        "date_of_birth": "1986-09-18",
        "nationality": "Indian",
        "passport_number": "CYKX23558",
        "passport_expiry_date": "2031-01-26"
    }
    ```
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if user already exists
    cursor.execute("SELECT id FROM users WHERE email = ?", (user.email,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash password
    hashed_password = get_password_hash(user.password)
    
    # Insert user
    cursor.execute("""
        INSERT INTO users (email, hashed_password, first_name, middle_name, last_name, 
                          phone_number, phone_country_code, date_of_birth, nationality,
                          passport_number, passport_expiry_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user.email, hashed_password, user.first_name, user.middle_name, user.last_name,
          user.phone_number, user.phone_country_code, user.date_of_birth, user.nationality,
          user.passport_number, user.passport_expiry_date))
    
    user_id = cursor.lastrowid
    conn.commit()
    
    # Get created user
    cursor.execute("""
        SELECT id, email, first_name, middle_name, last_name, phone_number, phone_country_code,
               date_of_birth, nationality, passport_number, passport_expiry_date, is_active,
               is_verified, created_at, last_login
        FROM users WHERE id = ?
    """, (user_id,))
    
    user_data = cursor.fetchone()
    conn.close()
    
    return UserResponse(**dict(user_data))

@router.post("/login")
async def login(user: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, email, hashed_password, first_name, middle_name, last_name,
               phone_number, phone_country_code, date_of_birth, nationality,
               passport_number, passport_expiry_date, is_active, is_verified,
               created_at, last_login, login_attempts, locked_until
        FROM users WHERE email = ?
    """, (user.email,))
    
    user_data = cursor.fetchone()
    if not user_data:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    user_dict = dict(user_data)
    
    # Check if account is locked
    if user_dict['locked_until'] and datetime.fromisoformat(user_dict['locked_until']) > datetime.now():
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is temporarily locked"
        )
    
    # Verify password
    if not verify_password(user.password, user_dict['hashed_password']):
        # Increment login attempts
        cursor.execute("""
            UPDATE users SET login_attempts = login_attempts + 1,
                           locked_until = CASE 
                               WHEN login_attempts >= 4 THEN datetime('now', '+15 minutes')
                               ELSE NULL
                           END
            WHERE id = ?
        """, (user_dict['id'],))
        conn.commit()
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Reset login attempts and update last login
    cursor.execute("""
        UPDATE users SET login_attempts = 0, locked_until = NULL, last_login = datetime('now')
        WHERE id = ?
    """, (user_dict['id'],))
    conn.commit()
    
    # Create access token
    access_token = create_access_token(data={"sub": str(user_dict['id'])})
    
    conn.close()
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user_dict['id'],
            "email": user_dict['email'],
            "first_name": user_dict['first_name'],
            "middle_name": user_dict['middle_name'],
            "last_name": user_dict['last_name']
        }
    }

@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, email, first_name, middle_name, last_name, phone_number, phone_country_code,
               date_of_birth, nationality, passport_number, passport_expiry_date, is_active,
               is_verified, created_at, last_login
        FROM users WHERE id = ?
    """, (current_user_id,))
    
    user_data = cursor.fetchone()
    conn.close()
    
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(**dict(user_data))

@router.put("/me", response_model=UserResponse)
async def update_current_user(user_update: UserUpdate, current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Build update query dynamically
    update_fields = []
    values = []
    
    for field, value in user_update.dict(exclude_unset=True).items():
        update_fields.append(f"{field} = ?")
        values.append(value)
    
    if not update_fields:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update"
        )
    
    values.append(current_user_id)
    
    cursor.execute(f"""
        UPDATE users SET updated_at = datetime('now'), {', '.join(update_fields)}
        WHERE id = ?
    """, values)
    
    conn.commit()
    
    # Get updated user
    cursor.execute("""
        SELECT id, email, first_name, middle_name, last_name, phone_number, phone_country_code,
               date_of_birth, nationality, passport_number, passport_expiry_date, is_active,
               is_verified, created_at, last_login
        FROM users WHERE id = ?
    """, (current_user_id,))
    
    user_data = cursor.fetchone()
    conn.close()
    
    return UserResponse(**dict(user_data))

@router.delete("/me")
async def delete_current_user(current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE id = ?", (current_user_id,))
    conn.commit()
    conn.close()
    
    return {"message": "User deleted successfully"}

# Passenger management routes
@router.post("/passengers", response_model=PassengerResponse)
async def create_passenger(passenger: PassengerCreate, current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO passengers (user_id, first_name, middle_name, last_name, date_of_birth,
                               passport_number, passport_expiry_date, passport_issuance_country,
                               nationality, gender, email, phone_number, phone_country_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (current_user_id, passenger.first_name, passenger.middle_name, passenger.last_name,
          passenger.date_of_birth, passenger.passport_number, passenger.passport_expiry_date,
          passenger.passport_issuance_country, passenger.nationality, passenger.gender,
          passenger.email, passenger.phone_number, passenger.phone_country_code))
    
    passenger_id = cursor.lastrowid
    conn.commit()
    
    # Get created passenger
    cursor.execute("""
        SELECT id, user_id, first_name, middle_name, last_name, date_of_birth,
               passport_number, passport_expiry_date, passport_issuance_country,
               nationality, gender, email, phone_number, phone_country_code, created_at
        FROM passengers WHERE id = ?
    """, (passenger_id,))
    
    passenger_data = cursor.fetchone()
    conn.close()
    
    return PassengerResponse(**dict(passenger_data))

@router.get("/passengers", response_model=List[PassengerResponse])
async def get_passengers(current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, user_id, first_name, middle_name, last_name, date_of_birth,
               passport_number, passport_expiry_date, passport_issuance_country,
               nationality, gender, email, phone_number, phone_country_code, created_at
        FROM passengers WHERE user_id = ? ORDER BY created_at DESC
    """, (current_user_id,))
    
    passengers = cursor.fetchall()
    conn.close()
    
    return [PassengerResponse(**dict(p)) for p in passengers]

@router.get("/passengers/{passenger_id}", response_model=PassengerResponse)
async def get_passenger(passenger_id: int, current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, user_id, first_name, middle_name, last_name, date_of_birth,
               passport_number, passport_expiry_date, passport_issuance_country,
               nationality, gender, email, phone_number, phone_country_code, created_at
        FROM passengers WHERE id = ? AND user_id = ?
    """, (passenger_id, current_user_id))
    
    passenger_data = cursor.fetchone()
    conn.close()
    
    if not passenger_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )
    
    return PassengerResponse(**dict(passenger_data))

@router.put("/passengers/{passenger_id}", response_model=PassengerResponse)
async def update_passenger(passenger_id: int, passenger_update: PassengerUpdate, 
                          current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if passenger exists and belongs to user
    cursor.execute("SELECT id FROM passengers WHERE id = ? AND user_id = ?", 
                   (passenger_id, current_user_id))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )
    
    # Build update query dynamically
    update_fields = []
    values = []
    
    for field, value in passenger_update.dict(exclude_unset=True).items():
        update_fields.append(f"{field} = ?")
        values.append(value)
    
    if not update_fields:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update"
        )
    
    values.append(datetime.now())
    values.append(passenger_id)
    
    cursor.execute(f"""
        UPDATE passengers SET updated_at = ?, {', '.join(update_fields)}
        WHERE id = ?
    """, values)
    
    conn.commit()
    
    # Get updated passenger
    cursor.execute("""
        SELECT id, user_id, first_name, middle_name, last_name, date_of_birth,
               passport_number, passport_expiry_date, passport_issuance_country,
               nationality, gender, email, phone_number, phone_country_code, created_at
        FROM passengers WHERE id = ?
    """, (passenger_id,))
    
    passenger_data = cursor.fetchone()
    conn.close()
    
    return PassengerResponse(**dict(passenger_data))

@router.delete("/passengers/{passenger_id}")
async def delete_passenger(passenger_id: int, current_user_id: int = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM passengers WHERE id = ? AND user_id = ?", 
                   (passenger_id, current_user_id))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )
    
    conn.commit()
    conn.close()
    
    return {"message": "Passenger deleted successfully"}
