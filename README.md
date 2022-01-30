# CLI for Weather
## Description

Using the Metaweather API, make a command line tool that receives a city name as an argument and says whether it’s going to rain tomorrow in this city or not.

Technologies: **Python, click, pytest**

## Build application

## Build application

Git clone the project: 

```
git clone https://github.com/GDemay/cli-trustpair.git
```

Build the image from the Dockerfile in the repository
```
docker build -t clitrustpair:latest .
```

Create a container from the image.

```
docker run -it clitrustpair
```

Execute the script

```
python3 app.py
```

### Getting the weather of tomorow for a city 
```
 python app.py weathertomorow nice
```

## Test

To test the API calls of this project, I decided to use Pytest.

To test the project:

```
pytest test_weather.py
```

Output:

```
(clienv) gdemay@DESKTOP-DEMAY-G:~/cli-trustpair$ pytest test_weather.py 
====================================================================================== test session starts =======================================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/gdemay/cli-trustpair
collected 6 items                                                                                                                                                                                

test_weather.py ......                                                                                                                                                                     [100%]

======================================================================================= 6 passed in 0.81s ========================================================================================
(clienv) gdemay@DESKTOP-DEMAY-G:~/cli-trustpair$ 
```
