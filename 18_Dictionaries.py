""" We use dictionaries to store key/value pairs.We can use strings or numbers to define keys.
    They should be unique. We can use any types for the value
"""

Alok_dict = {
    "name": "Alok",
    "email": "aloksri2204@gmail.com",
    "Age": 27,
    "is_verifed": True
}
print(Alok_dict)
print(Alok_dict ["name"])
print(Alok_dict.get("email", "abc"))
print(Alok_dict.get("id", "123"))
Alok_dict["name"] = "Rishu"
print(Alok_dict)
print(Alok_dict.get("name"))
Alok_dict["roll_no"] =4
print(Alok_dict)

