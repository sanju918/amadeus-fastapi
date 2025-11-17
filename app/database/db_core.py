import sqlite3
from pathlib import Path

# Define the database file path
DB_FILE = Path("flight_booking.db")

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    # Set row_factory to sqlite3.Row to access columns by name
    conn.row_factory = sqlite3.Row 
    return conn

def create_users_table():
    """Creates the 'users' table if it doesn't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL to create the enhanced users table with JWT support
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            phone_number TEXT,
            phone_country_code TEXT DEFAULT '+1',
            date_of_birth DATE,
            nationality TEXT,
            passport_number TEXT,
            passport_expiry_date DATE,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            is_verified BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            login_attempts INTEGER DEFAULT 0,
            locked_until TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def create_passengers_table():
    """Creates the 'passengers' table if it doesn't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL to create the passengers table with foreign key to users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            passport_number TEXT NOT NULL,
            passport_expiry_date DATE NOT NULL,
            passport_issuance_country TEXT NOT NULL,
            nationality TEXT NOT NULL,
            gender TEXT NOT NULL CHECK (gender IN ('MALE', 'FEMALE', 'OTHER')),
            email TEXT,
            phone_number TEXT,
            phone_country_code TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    conn.close()

# Run the functions to ensure the database file and tables exist
create_users_table()
create_passengers_table()
print(f"Database '{DB_FILE}', 'users' and 'passengers' tables initialized.")