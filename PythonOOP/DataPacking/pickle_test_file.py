# doplnit od učitele
import pickle
import string
import os
from car import Car

# Function to create a full path for the file.
def create_path(file_name):
    # Get the directory of the current script.
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Return the full path.
    return os.path.join(script_dir, file_name)

# Function to serialize data and save it to a file.
def serialize(file_name, data):
    # Open the file in binary write mode and save the serialized data to it.
    with open(create_path(file_name), "wb") as file:
         pickle.dump(data, file)

# Function to load data from a file and deserialize it.
def deserialize(file_name):
    # Open the file in binary read mode, load and deserialize the data from it.
    with open(create_path(file_name), "rb") as file:
         data = pickle.load(file)
    return data

try:
    # Create a list of lowercase English letters.
    c = Car("audi", "black")
    file_name = "letters.dat"

    # Print the original list.
    print(f"Original data:\n{c}\n")

    # Serialize the list and write it to a file.
    serialize(file_name, c)
    # Read the file, deserialize its content and store it in 'letters_restored'.
    c_restored = deserialize(file_name)

    # Print the deserialized list.
    print(f"Deserialized data:\n{c_restored}\n")

# Handle any exceptions that might occur during the process.
except Exception as e:
    print(e)