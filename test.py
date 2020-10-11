import requests
import time


api_key = "27bef37f32dfd5a6298e9540d63fda01"

weather_url = "http://api.openweathermap.org/data/2.5/weather?"
#start of the program
print("Welcome to my program!")
time.sleep(1)
print("Where would you like to check the weather?")
time.sleep(1)
city_zip_code = input(f"Enter city or zip code here: ")


complete_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_zip_code}&appid={api_key}&units=imperial'
response = requests.get(complete_url)
x = response.json() #connects to open weather map


def weatherConnection(): #allows user to run program and try new cities or zip

  restart = input(f"Would you like to search again? ").lower()
  if restart == "yes" or restart == 'y':
    city_zip_code_new = input(f"Enter new city or zip code: ")
    new_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_zip_code_new}&appid={api_key}&units=imperial'
    response = requests.get(new_url)
    x = response.json()
    if x["cod"] != "404":
      y = x["main"]
      current_temperature = y["temp"] #displays temp in fahrenheit
      current_humidity = y["humidity"]
      z = x["weather"]
      weather_condition = z[0]["description"]
      print(f"\n Temperature (in Fahrenheit) = " +
            str(current_temperature) +
            "\n Humidity (in Percentage) = " +
            str(current_humidity) +
            "\n Conditions = " +
            str(weather_condition))
      weatherConnection()
    else:
      print(" Sorry, that was not valid. Please try again or quit. ")

  else:
    print("Thanks for checking the weather!")


def main():
  if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_condition = z[0]["description"]
    print(f"\n Temperature (in Fahrenheit) = " +
          str(current_temperature) +
          "\n Humidity (in Percentage) = " +
          str(current_humidity) +
          "\n Conditions = " +
          str(weather_condition))
  else:
    print(" Sorry, that was not valid. Please try again or quit. ")

  weatherConnection()

try:
    response = requests.get(complete_url) #testing connection to weather service

    print(f"\nConnecting to the weather map...")
    print(f"\nConnection was successful!")

except:
    print("We can't connect you, please try again.")

main()
