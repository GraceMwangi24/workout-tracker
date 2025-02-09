
from lib.db.models import session, Base ,Workout, User, Exercise
from lib.db.models import init_db


def seed_data():
    user1 = User(name="Grace")
    user2 = User(name="Elvis")

    workout1 = Workout(name = "Leg Day", user=user2)
    workout2 = Workout(name = "Upper Body", user=user1)
    workout3 = Workout(name = "Core", user=user1)

    exercise1 = Exercise(name="Back Squats", reps= 12, workout =workout1)
    exercise2 = Exercise(name="Lat Pulldowns", reps= 10, workout =workout2)
    exercise3 = Exercise(name="Crunches", reps= 10, workout =workout3)

    session.add_all([user1,user2,workout1,workout2,workout3,exercise1,exercise2,exercise3])
    session.commit()
    print ("Database seeded successfully!")

if __name__== "__main__":
    init_db()
    seed_data()    