'''
Find the angle between the Hour hand and the Minute hand when the user 
inputs the time in the hh:mm format
Input : 10:30
Output : 135
'''

def clockangle(hr, mins):
	if(mins==60):
		hr+=1
		mins=0
	if(hr==12):
		hr=0
	hrangle = 0.5 * ((hr*60) + mins)
	minangle = 6 * mins

	angle = abs(hrangle - minangle)
	return angle

print("Enter time in hh:mm format")
time = input()
hour = time[0] + time[1]
minute = time[3] + time[4]
hour = int(hour)
minute = int(minute)
if(hour < 0 or minute < 0 or hour > 12 or minute > 60):
	print("Invalid time input")
else:
	result = clockangle(hour, minute)
	print("The angle is {0}".format(result))
