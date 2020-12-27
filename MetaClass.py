"""Create metaclass with inheritance"""

Box = type("Box", (), {"hummer": True, "screwdriver": False})


NewBox = type("NewBox", (Box,), {"screw": 5})

print(NewBox.hummer, NewBox.screw, sep="\n")

