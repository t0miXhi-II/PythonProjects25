import request

def main():
    WEATHER_APP_API = ""
    city = input("Enter city name: ")

    #API CALL
    response = request.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_APP_API}")
    data = response.json()

    print(f"Weather in {city}: {data['weather'][0]['description']}")


if __name__ == "__main__":
    main()