# checks the current time and wait time for user input
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

# convert dtring inputs to intergers 
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# calculate the final time and wrap around
finalTimeInt = (currentTimeInt + waitTimeInt) % 24
# print the final time 
print(finalTimeInt)
