import click
from lib.db.models import init_db
from lib.utils import add_user, list_users, add_workout,list_workouts
from lib.db.seed import seed_data


@click.group()
def cli():
    """Workout Tracker CLI"""
    pass

@click.command()
@click.argument('name')
def create_user(name):
    """Create a new user"""
    add_user(name)
    click.echo(f"user '{name}' created successfully!")

@click.command()
def show_users():
    """List all users"""
    users = list_users()
    if users:
        click.echo("Users:")
        for user in users:
            click.echo(f"- {user}")
    else:
        click.echo("No users found.")
    
        

@click.command()
@click.argument('user_name')
@click.argument('workout_name')
def create_workout(user_name, workout_name):
    """Add a workout for a user"""
    add_workout(user_name,workout_name)
    click.echo(f"Workout '{workout_name}' added for {user_name}.")

@click.command()
@click.argument('user_name')
def show_workouts (user_name):
    """List workouts for a user"""
    workouts = list_workouts(user_name)
    if isinstance(workouts, list) and workouts:
        click.echo(f"Workouts for {user_name}:")
        for workout in workouts:
            click.echo(f"- {workout}")
    else:
        click.echo(f"No workouts found for {user_name}.")

@click.command()
def seed_db():
    """Seed the database with sample data"""
    seed_data()
    click.echo("Database seeded successfully!")

cli.add_command(create_user)
cli.add_command(show_users)       
cli.add_command(create_workout)
cli.add_command(show_workouts)

if __name__ == '__main__':
    init_db()
    seed_data()
    cli()