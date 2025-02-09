from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Create engine 
DATABASE_URL = "sqlite:///workout.db"
Base = declarative_base()

#tables 
class User(Base):
    __tablename__= 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)

    workouts = relationship('Workout', back_populates='user')

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='workouts')
    exercises = relationship('Exercise', back_populates='workout')

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    reps = Column(Integer)
    workout_id = Column(Integer, ForeignKey('workouts.id'))

    workout = relationship('Workout', back_populates='exercises')



engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Database and tables created successfully!")
