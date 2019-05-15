import pyowm

owm = pyowm.OWM('fdadb56d09379ae0020c29800194f6ce')

city=input(' Whats city are you wanting?(max 3 tried) : ')

observation = owm.weather_at_place(city)
w = observation.get_weather()

print(' In the city of ' + city + ' is now the temperature outside = ' + str(w.get_temperature('celsius')))
again=input(' Do you want to exit? : ')
if again=='yes':
	exit()
elif again=='no':
	city=input(' Whats city are you wanting?(left 2 tried) : ')
	observation = owm.weather_at_place(city)
	w = observation.get_weather()
	print(' In the city of ' + city + ' is now the temperature outside = ' + str(w.get_temperature('celsius')))
	again=input(' Do you want to exit? : ')
	if again=='yes':
		exit()
	elif again=='no':
			city=input(' Whats city are you wanting?(the last tried) : ')
			observation = owm.weather_at_place(city)
			w = observation.get_weather()
			print(' In the city of ' + city + ' is now the temperature outside = ' + str(w.get_temperature('celsius')))
			exit=str(input(' Enter 0 or 1 to exit please: '))
			if str(exit)=='1':
				str(exit())
			elif str(exit)=='k':
				str(exit())
			else:
				exit()