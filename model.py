
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class WeatherForecast(Base):
    __tablename__ ='weather'
    id = db.Column(db.Integer, primary_key=True ,autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    raind = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    good_condition = db.Column(db.Boolean, default=False)
    bad_condition = db.Column(db.Boolean, default=False)  

      
      


