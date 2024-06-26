# Import the json module for handling JSON data
# Import os module for operating system dependent functionality
import json
import os
from car import Car

# Define a function to create a full file path
def create_path(file_name):
    # Get the directory of the script being run
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Join the script directory and the file name to create a full file path
    return os.path.join(script_dir, file_name)

# Define a function to serialize and save data to a file
def serialize(file_name, data):
    # Create a full file path
    path = create_path(file_name)
    # Open the file in write mode
    with open(path,"w") as file:
        # Serialize and save data to the file
        json.dump(data.to_json(), file)

# Define a function to load data from a file and deserialize it
def deserialize(file_name):
    # Create a full file path
    path = create_path(file_name)
    # Open the file in read mode
    with open(path, "r") as file:
        # Load and deserialize data from the file
        data = json.load(file)
    # Return the deserialized data
    return data

# Main execution
try:
    # Define file name
    file_name = "employee.dat"
    # Define dictionary to store employee data
    c = Car("audi", "black")
    # Serialize and save the employee dictionary to a file
    serialize(file_name, c)
    # Print the dictionary before saving to file
    print(f"Before saving to file:\n{c}\n")
    # Load the data from the file and deserialize it
    deserialized_c = deserialize(file_name)
    # Print the deserialized dictionary after loading from file
    print(f"After loading from file:\n{deserialized_c}\n")

    new_c = Car(deserialized_c["name"], deserialized_c["color"])
    print(new_c)

# Handle any exceptions that occur during the execution
except Exception as e:
    print(e)