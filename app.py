import click
import requests

def getWoeidFromCity(city): 
    '''
    Get the woeid from a city name
    woeid is a unique identifier for a location
    '''
    try:
      return requests.get(f'https://www.metaweather.com/api/location/search/?query={city}') 
    except Exception as e:
      click.secho(f' Something wrong happened with this city {city}', fg='red', bold=True)
      exit(1)

def getWeatherFromWoeid(woeid):
  '''
  Get the weather from a woeid
  '''
  try:
    return requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
  except Exception as e:
    click.secho(f'Something wrong happened with this woeid {woeid}', fg='red', bold=True)
    exit(1)

def isItRainning(weatherState):
  '''
  Check if from the weatherState we can tell if it is rainning
  '''
  rainState = ["sn", "sl", "h", "hr", "lr", "s"]
  if weatherState in rainState:
    return True
  return False


@click.group()
def cli():
  pass

@click.command()
@click.argument('city')
def weatherTomorow(city):
    """
    Tells if it's rainning tomorrow by giving city name.
    """

    #Get the woeid
    woeid = getWoeidFromCity(city).json()
    if not woeid:
      click.secho(f' City name is wrong: {city}', fg='red', bold=True)
      exit(1)
    
    woeid = woeid[0]['woeid']
    # Get the weather
    weather = getWeatherFromWoeid(woeid).json()
    if not weather:
      click.secho(f' Error while getting data for {city}', fg='red', bold=True)
      exit(1)
      
    # We have 5 days of weather, [0] is today, [1] is tomorow, [2] is the day after etc...
    weather_tomorrow = weather['consolidated_weather'][1]
    weather_state = weather_tomorrow['weather_state_abbr']
    
    
    if isItRainning(weather_state):
      click.secho(f' It is rainning tomorrow in {city} 🌧️', fg='blue')
      return True
    else:
      click.secho(f'It won\'t rain in {city} tomorow 😊', fg='yellow')
      return False

cli.add_command(weatherTomorow)

if __name__ == '__main__':
  cli()