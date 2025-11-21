from fastapi import FastAPI
from app.api import auth, bets, stats

app = FastAPI(title="Sports Investor API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bets.router, prefix="/bets", tags=["Bets"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])

@app.get("/")
def root():
    return {"message": "Sports Investor API running"}
