from app import *

def test_getLondonWoeid():
  '''
    Test if API returns London woeid
  '''
  assert (getWoeidFromCity('London').json()[0]['woeid'] == 44418)
  
def test_getParisWoeid():
  '''
    Test if API returns Paris woeid
  '''
  assert (getWoeidFromCity('Paris').json()[0]['woeid'] == 615702)
  
def test_getBadCity():
  '''
    Test by giving a bad city name
  '''
  assert (len(getWoeidFromCity('WrongCityName').json()) == 0)
  
def test_getWeatherFromWoeid():
  '''
  test if API returns a dictionary
  '''
  LondonWoeid = getWoeidFromCity('London').json()[0]['woeid']
  LondonWeather = getWeatherFromWoeid(LondonWoeid).json()
  assert (type(LondonWeather) == dict)

def test_rain():
  '''
    Test if API returns a good rain state (available here: https://www.metaweather.com/api/)
  '''
  assert(isItRainning("sn") == True)
  
def test_notRain():
  '''
  Test if API returns a good rain state (available here: https://www.metaweather.com/api/)
  '''
  assert(isItRainning("c") == False)
  
