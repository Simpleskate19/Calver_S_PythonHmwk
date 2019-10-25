# Check a temperature and output a result
# 
temperature = int(input("input a number between o and 100"))

if temperature <= 4:
	print("water is a solid cuz it's frozen")

elif temperature < 100:
	print("water is a liquid")

else:
	print("water is a gas cuz its boiling!")

