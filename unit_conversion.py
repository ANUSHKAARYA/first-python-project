#First create dictionaries for measurements and their conversion factors.
inches_conversions = {
    "inches": 1,
    "feet": 1/12,
    "yards": 1/36,
    "miles": 1/63360,
    "millimeters": 25.4,
    "centimeters": 2.54,
    "meters": 0.0254,
    "kilometers": 0.0000254
}

feet_conversions = {
    "inches": 12,
    "feet": 1,
    "yards": 1/3,
    "miles": 1/5280,
    "millimeters": 304.8,
    "centimeters": 30.48,
    "meters": 0.3048,
    "kilometers": 0.0003048
}

yards_conversions = {
    "inches": 36,
    "feet": 3,
    "yards": 1,
    "miles": 1/1760,
    "millimeters": 914.4,
    "centimeters": 91.44,
    "meters": 0.9144,
    "kilometers": 0.0009144
}

miles_conversions = {
    "inches": 63360,
    "feet": 5280,
    "yards": 1760,
    "miles": 1,
    "millimeters": 1609344,
    "centimeters": 160934.4,
    "meters": 1609.344,
    "kilometers": 1.609344
}

millimeters_conversions = {
    "inches": 0.0393701,
    "feet": 0.00328084,
    "yards": 0.00109361,
    "miles": 0.000000621371,
    "millimeters": 1,
    "centimeters": 0.1,
    "meters": 0.001,
    "kilometers": 0.000001
}

centimeters_conversions = {
    "inches": 0.393701,
    "feet": 0.0328084,
    "yards": 0.0109361,
    "miles": 0.00000621371,
    "millimeters": 10,
    "centimeters": 1,
    "meters": 0.01,
    "kilometers": 0.00001
}

meters_conversions = {
    "inches": 39.3701,
    "feet": 3.28084,
    "yards": 1.09361,
    "miles": 0.000621371,
    "millimeters": 1000,
    "centimeters": 100,
    "meters": 1,
    "kilometers": 0.001
}

kilometers_conversions = {
    "inches": 39370.1,
    "feet": 3280.84,
    "yards": 1093.61,
    "miles": 0.621371,
    "millimeters": 1000000,
    "centimeters": 100000,
    "meters": 1000,
    "kilometers": 1
}

# Take in a meaurement amount float, take in the unit of measurement, then take in the unit of measurement to convert to.
unit = input("What unit do you want to convert from? ")
unit = unit.lower()

measurement = float(input("Enter the value of the measurement: "))

unit_conversion = input("Enter the unit of measurement to convert to: ")
unit_conversion = unit_conversion.lower()


# Convert the measurement to the new unit of measurement and print the result.
if unit == "inches":
    print(measurement * inches_conversions[unit_conversion])
elif unit == "feet":
    print(measurement * feet_conversions[unit_conversion])
elif unit == "yards":
    print(measurement * yards_conversions[unit_conversion])
elif unit == "miles":
    print(measurement * miles_conversions[unit_conversion])
elif unit == "millimeters":
    print(measurement * millimeters_conversions[unit_conversion])
elif unit == "centimeters":
    print(measurement * centimeters_conversions[unit_conversion])
elif unit == "meters":
    print(measurement * meters_conversions[unit_conversion])
elif unit == "kilometers":
    print(measurement * kilometers_conversions[unit_conversion])
else:
    print("The unit of measurement entered has to be a distance measurement. (i.e. inches, feet, yards, miles, millimeters, centimeters, meters, kilometers)")