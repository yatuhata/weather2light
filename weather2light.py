#coding:utf-8

import json
import pyowm
import pytz
import datetime

owm      = pyowm.OWM('your_api_key')  # You MUST provide a valid API key
LOCATION = "Tokyo,jp"
TIMEZONE = pytz.timezone("Asia/Tokyo")

fcr      = owm.three_hours_forecast(LOCATION)	# forecaster object
fc       = fcr.get_forecast()			# forecast object
weathers = fc.get_weathers()

print( 'time  weather clouds[%] temp[`C] max[`C] min[`C]' )
for w in weathers:
	time_unix = w.get_reference_time()
	time_jst  = datetime.datetime.fromtimestamp(time_unix, tz=TIMEZONE)
	weather   = w.get_detailed_status()
	clouds    = w.get_clouds()
	temp      = w.get_temperature('celsius')['temp']
	temp_max  = w.get_temperature('celsius')['temp_max']
	temp_min  = w.get_temperature('celsius')['temp_min']
	print( time_jst, weather, clouds, temp, temp_max, temp_min )
