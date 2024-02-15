distance = 5

if distance < 3:
    medium = "Walk"
elif distance <= 15:
    medium = "Bike"
else:
    medium = "Car"

print("AI recommends you the transport medium of :", medium)