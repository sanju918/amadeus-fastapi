from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.apis.flight_offers_search import router as flight_offers_router, airline_router
from app.apis.auth_routes import router as auth_router
from app.database.db_core import create_users_table, create_passengers_table

# Initialize database tables
create_users_table()
create_passengers_table()

app = FastAPI(
    title="Flight Booking API",
    description="A FastAPI application for flight search and booking with user authentication",
    version="0.1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "initialized"}

# Include routers
app.include_router(flight_offers_router)
app.include_router(airline_router)
app.include_router(auth_router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
