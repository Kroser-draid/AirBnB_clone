#!/usr/bin/python3
from models import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
# Add attributes to the instance
my_model.name = "My First Model"
my_model.my_number = 89
# Print the instance
print(my_model)
# Save the instance to update the updated_at attribute
my_model.save()
# Print the instance again to see the updated updated_at
print(my_model)
# Convert the instance to a dictionary
my_model_json = my_model.to_dict()
# Print the dictionary representation
print(my_model_json)
# Print each key-value pair in the dictionary
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
