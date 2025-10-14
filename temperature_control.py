# It receives temperature information from the user and prints the temperature status on the screen.
print("Hello User :)")
print("Welcome to Temperature Control System...")
temperature_control = int(input("Please, enter the degree of temperature: "))
if temperature_control > 30:
    print(f"The weather is very hot. The degree of temperature: {temperature_control}")
elif 20 < temperature_control < 30:
    print(f"The weather is warm. the degree of temperature: {temperature_control}")
elif temperature_control < 20:
    print(f"The weather is very cold. The degree of temperature: {temperature_control}")
else:
    print("Unknown msitake!")
