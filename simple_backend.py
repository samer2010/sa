from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="TechVerse Simple API",
    description="Simple backend for TechVerse frontend demonstration",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3003", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "TechVerse Simple API is running",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to TechVerse Simple API",
        "version": "1.0.0",
        "modules": [
            "TechLearn - Interactive Education",
            "TechMarket - Comprehensive Marketplace", 
            "TechHub - Professional Community",
            "TechConnect - Secure Communication",
            "TechFinance - Advanced Finance Platform",
            "TechInnovation - Innovation Ecosystem"
        ]
    }

# Mock endpoints for frontend
@app.get("/api/users/me")
async def get_current_user():
    return {
        "id": 1,
        "username": "demo_user",
        "email": "demo@techverse.com",
        "full_name": "Demo User",
        "role": "user"
    }

@app.get("/api/techconnect/chats")
async def get_chats():
    return {
        "chats": [
            {
                "id": 1,
                "name": "Tech Innovation Group",
                "last_message": "Welcome to TechVerse!",
                "unread_count": 0
            },
            {
                "id": 2, 
                "name": "Finance Discussion",
                "last_message": "New investment opportunities",
                "unread_count": 3
            }
        ]
    }

@app.get("/api/techfinance/wallet")
async def get_wallet():
    return {
        "balance": 1500.50,
        "currency": "USD",
        "transactions": [
            {"id": 1, "amount": 100, "type": "deposit", "date": "2024-01-15"},
            {"id": 2, "amount": -50, "type": "withdrawal", "date": "2024-01-14"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)