import enum
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker 
  
engine = create_engine('sqlite:///gfg.db') 
Base = declarative_base() 
Session = sessionmaker(bind=engine) 
session = Session() 


class GenderEnum(enum.Enum):
    FEMENINO = "Femenino"
    MASCULINO = "Masculino"
    
class Pacient(Base): 
    __tablename__ = 'pacients'
      
    id = Column(Integer, primary_key=True) 
    name = Column(String) 
    last_name = Column(String)
    bike_name = Column(String)
    age = Column(Integer) 
    weigth = Column(Float)
    height = Column(Float)
    gender = Column(Enum(GenderEnum))
    url_video = Column(String)  
    knee_min = Column(Float)
    knee_max = Column(Float)
    hip_min = Column(Float)
    hip_max=Column(Float)
    shoulder_avg=Column(Float)
    hip_translation_horizontal=Column(Float)
    hip_translation_vertical=Column(Float)
      
    # fees = relationship("Fee") 
Base.metadata.create_all(engine)