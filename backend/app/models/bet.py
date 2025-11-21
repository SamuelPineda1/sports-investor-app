from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    league = Column(String)
    team = Column(String)
    stake = Column(Float)
    odds = Column(Float)
    status = Column(String) # pending, won, lost
    image_url = Column(String)

    user = relationship("User", back_populates="bets")
