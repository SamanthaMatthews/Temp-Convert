
print("Please choose an option below.")
print("1. Convert Fahrenheit to Celsius")
print("2. Convert Celsius to Fahrenheit")
print("0. Exit the program")

menuChoice = input()

if menuChoice == "1":
	
	print("What is the temperature in Fahrenheit?")

	userTempInFahrenheit = float(input())

	userTempInCelcius = (userTempInFahrenheit - 32) *(5/9)

	print("In that case, the temperature is " + str(userTempInCelcius) + " degrees Celsius")

elif menuChoice == "2":
	print("What is the temperature in Celsuis?")
	
	userTempInCelcius = float(input())
	
	userTempInFahrenheit = (userTempInCelcius * 9/5) + (32)
	
	print("In that case, the temperature is " + str(userTempInFahrenheit) + " degrees Fahrenheit.")
else:
	print("Have a good day!")