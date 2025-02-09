from src.database import Base
from sqlalchemy import Column, Computed, Date, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Trip(Base):

    __tablename__ = "Trip"

    id = Column(Integer, primary_key=True, nullable=False)
    company = Column(Integer, nullable=False) 
    plane = Column(String, nullable=False)
    town_from = Column(String, nullable=False)
    town_to = Column(String, nullable=False)
    time_out = Column(DateTime, nullable=False)
    time_in = Column(DateTime, nullable=False)


class Company(Base):

    __tablename__ = "Company"

    id = Column(Integer, ForeignKey('Trip.company'), primary_key=True, nullable=False)
    name = Column(String, nullable=False) 


class PassInTrip(Base):

    __tablename__ = "PassInTrip"

    id = Column(Integer, primary_key=True, nullable=False)
    trip = Column(Integer, ForeignKey("Trip.id"), nullable=False) 
    passenger = Column(Integer, ForeignKey("Passenger.id"), nullable=False) 
    place = Column(String, nullable=False) 


class Passenger(Base):

    __tablename__ = "Passenger"

    id = Column(Integer, ForeignKey('Trip.company'), primary_key=True, nullable=False)
    name = Column(String, nullable=False) 