from lib.db.models import session, User, Workout, Exercise

def list_users():
    users = session.query(User).all()
    return [user.name for user in users]

def add_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")

def list_workouts(user_name):
    user = session.query(User).filter_by(name=user_name).first()
    if user:
        return [workout.name for workout in user.workouts]
    else:
        return f"No workouts found for {user_name}."

def add_workout(user_name, workout_name):
    user = session.query(User).filter_by(name=user_name).first()
    if user:
        workout = Workout(name=workout_name, user=user)
        session.add(workout)
        session.commit()
        print(f"Workout '{workout_name}' added to {user_name}.")
    else:
        print("User not found.")
