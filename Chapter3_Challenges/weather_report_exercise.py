"""""

Weather Report
In this exercise you will create a weather reporting function that takes another function as its argument.

Here are some instructions:

Declare a function called report_weather that takes a temperature and a function as its two arguments
Declare two other functions, each of which takes a temperature as an argument
One is called as_sun_lover and it returns 'great' if the temp is 25 Celsius, or above. Otherwise it returns 'not great'
One is called as_snow_lover and it returns 'great' if the temp is 0, or below. Otherwise it returns 'not great'
Combine the functions to generate customised weather reports

"""



def as_sun_lover(temperature):
    if temperature >= 25:
        return "Great"
    else:
        return "Not Great"
    
def as_snow_lover(temperature):
    if temperature <= 0:
        return "Great"
    else:
        return "Not Great"

def weather_report(temperature, as_sun_lover):
    report = as_sun_lover(temperature)
    return report 

def weather_report2(temperature, as_sun_lover):
    report2 = as_snow_lover(temperature)
    return report2
