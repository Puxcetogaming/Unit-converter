def distance_converter():
    distance = float(input("Enter the distance: "))
    unit = input("Enter the unit (km/mi/m): ")
    if unit == "km":
        distance_m = distance * 1000
    elif unit == "mi":
        distance_m = distance * 1609.34
    elif unit == "m":
        distance_m = distance
    else:
        print("Invalid unit")
        return
    output_unit = input("Enter the output unit (km/mi/m): ")
    if output_unit == "km":
        output_distance = distance_m / 1000
    elif output_unit == "mi":
        output_distance = distance_m / 1609.34
    elif output_unit == "m":
        output_distance = distance_m
    else:
        print("Invalid output unit")
        return
    print(f"{distance} {unit} is equal to {output_distance} {output_unit}")

def speed_converter():
    speed = float(input("Enter the speed: "))
    unit = input("Enter the unit (km/h/mph/m/s): ")
    if unit == "km/h":
        speed_mps = speed / 3.6
    elif unit == "mph":
        speed_mps = speed * 0.44704
    elif unit == "m/s":
        speed_mps = speed
    else:
        print("Invalid unit")
        return
    output_unit = input("Enter the output unit (km/h/mph/m/s): ")
    if output_unit == "km/h":
        output_speed = speed_mps * 3.6
    elif output_unit == "mph":
        output_speed = speed_mps / 0.44704
    elif output_unit == "m/s":
        output_speed = speed_mps
    else:
        print("Invalid output unit")
        return
    print(f"{speed} {unit} is equal to {output_speed} {output_unit}")

def weight_converter():
    weight = float(input("Enter the weight: "))
    unit = input("Enter the unit (kg/lb): ")
    if unit == "kg":
        weight_kg = weight
    elif unit == "lb":
        weight_kg = weight * 0.453592
    else:
        print("Invalid unit")
        return
    output_unit = input("Enter the output unit (kg/lb): ")
    if output_unit == "kg":
        output_weight = weight_kg
    elif output_unit == "lb":
        output_weight = weight_kg / 0.453592
    else:
        print("Invalid output unit")
        return
    print(f"{weight} {unit} is equal to {output_weight} {output_unit}")

def height_converter():
    height = float(input("Enter the height: "))
    unit = input("Enter the unit (cm/in): ")
    if unit == "cm":
        height_m = height / 100
    elif unit == "in":
        height_m = height * 0.0254
    else:
        print("Invalid unit")
        return
    output_unit = input("Enter the output unit (cm/in): ")
    if output_unit == "cm":
        output_height = height_m * 100
    elif output_unit == "in":
        output_height = height_m / 0.0254
    else:
        print("Invalid output unit")
        return
    print(f"{height} {unit} is equal to {output_height} {output_unit}")



print("Welcome to the converter")
print("The available conversions are: distance, speed, weight, height")
User_Choice = input("Enter the type of conversion (distance/speed/weight/height): ")

if User_Choice == "distance":
    distance_converter()
elif User_Choice == "speed":
    speed_converter()
elif User_Choice == "weight":
    weight_converter()
elif User_Choice == "height":
    height_converter()
else:
    print("Invalid conversion type")