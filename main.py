from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.apis.flight_offers_search import router as flight_offers_router, airline_router

app = FastAPI(
    title="FastAPI with UV",
    description="A FastAPI application using UV package manager",
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
    return {"message": "Welcome to FastAPI with UV!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Include flight offers search router
app.include_router(flight_offers_router)
app.include_router(airline_router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
