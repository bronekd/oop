
#moje řešení:
"""
import pickle
from PythonOOP.car import Car


numbers = [1,2,3,4,5,6]
c = Car("audi", "black")

print ("Prvni Car: ", c)

serialized_data = pickle.dumps(c)

print (f"Serialized data : \n{serialized_data}\n")

deserated_data = pickle.loads(serialized_data)
"""




# Importing 'pickle' module, used for object serialization and deserialization.
import pickle
from PythonOOP.car import Car

# Creating a list of numbers.
numbers = [1, 2, 3, 4, 5]
c = Car("audi", "black")

print("prvni car: ", c)
# Serializing the list to a bytes object.
serialized_data = pickle.dumps(c)

# Printing the serialized data.
print(f"Serialized data:\n{serialized_data}\n")

# Deserializing the bytes back into a list.
deserialized_data = pickle.loads(serialized_data)

# Printing the deserialized data.
print(f"Deserialized data:\n{deserialized_data}\n")