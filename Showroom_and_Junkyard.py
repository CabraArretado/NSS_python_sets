showroom = set()

showroom.add("Truck")
showroom.add("Sedan")
showroom.add("Jeep")
showroom.add("Bug")


# print(len(showroom))

showroom.add("Jeep")
showroom.update({"Monster Truck", "Semi-Sedand"})
showroom.discard("Semi-Sedand")

# print(showroom)

junkyard = {"Semi-Sedand", "Super Truck"}
junkyard.update({"Sedan", "Bug"})

print(showroom.intersection(junkyard))

showroom = showroom.union(junkyard)
print(showroom)

showroom.discard("Super Truck")

print(showroom)