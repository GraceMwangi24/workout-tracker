## Database Schema

Here is the schema for the Workout Tracker database:

https://dbdiagram.io/d/67a8fdf5263d6cf9a089ff25
# Workout Tracker CLI

A simple command-line interface (CLI) application for tracking workouts, users, and routines. This project uses SQLAlchemy as the ORM to interact with a SQLite database and Click to manage CLI commands.
## Overview

The Workout Tracker CLI allows you to:
- Create users.
- Add workouts and assign them to users.
- Seed the database with sample workout data.
- Retrieve workout details from the database.

## Features

- Add User:Create a new user.
- Add Workout:Add a new workout and assign it to a user.
- List Workouts: Retrieve and display workouts from the database.
- Seed Data: Populate the database with sample workout data.

Seeding the Database
python lib/workout_tracker.py seed

Create a User:
python lib/workout_tracker.py create-user <name>

List All Users:
python lib/workout_tracker.py show-users

Add a Workout for a User:
python lib/workout_tracker.py create-workout <user_name> <workout_name>

Show Workouts for a User:
python lib/workout_tracker.py show-workouts <user_name>