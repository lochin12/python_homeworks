def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32
def convert_far_to_cel(fahrengeit):
    return (fahrengeit - 32) * 5 / 9
far = float(input("Enter a temperature in degrees F: "))
cel = convert_far_to_cel(far)
print(f"{far} degrees F = {round(cel, 2)} degrees C")
cel = float(input("Enter a temperature in degrees C: "))
far = convert_cel_to_far(cel)
print(f"{cel} degrees C = {round(far, 2)} degrees F")
