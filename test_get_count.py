#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Print the total number of objects
print("All objects: {}".format(storage.count()))

# Print the number of State objects
print("State objects: {}".format(storage.count(State)))

# Retrieve all State objects
all_states = list(storage.all(State).values())

# Check if there are any State objects before accessing the first one
if all_states:
    first_state_id = all_states[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found.")
