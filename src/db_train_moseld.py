from src.database import Base
from sqlalchemy import Column, Computed, Date, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

######## АВИАПЕРЕЛЁТЫ ##########
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

######## СЕМЬЯ ##########
class FamilyMembers(Base):

    __tablename__ = "FamilyMembers"

    member_id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String, nullable=False) 
    member_bame = Column(String, nullable=False) 
    birthday = Column(DateTime, nullable=False) 


class GoodTypes(Base):

    __tablename__ = "GoodTypes"

    good_type_id = Column(Integer, primary_key=True, nullable=False)
    good_time_name = Column(String, nullable=False) 


class Goods(Base):

    __tablename__ = "Goods"

    good_id = Column(Integer, primary_key=True, nullable=False)
    good_name = Column(String, nullable=False) 
    type = Column(String, ForeignKey("GoodTypes.good_type_id"), nullable=False) 


class Payments(Base):

    __tablename__ = "Payments"

    payment_id = Column(Integer, primary_key=True, nullable=False)
    family_member = Column(String, ForeignKey("FamilyMembers.member_id"), nullable=False) 
    good = Column(String, ForeignKey("Goods.good_id"), nullable=False)
    amount = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)