import requests
import sys

def main():
    while True :
        try :
            city = input("Enter city name: ")

        except EOFError :
            print()
            sys.exit()

        else :
            with open("city.csv") as file :
                lines = [line.strip().split(",") for line in file]
                for i in range(len(lines)):
                    if city in lines[i][0]:
                        get_weather(city)
                        sys.exit()
                    else :
                        continue
                print("city not found")
                continue


def get_weather(city):
    api_key = "gmvH4TaiHlYRF1WOzZpFfwDDVcg2aFvJ"
    base_url = "https://api.tomorrow.io/v4/weather/forecast"
    params = {
        "location" : city,
        "apikey" : api_key,
        "timelines" : "1h",
        "units" : "metric"
        }

    try :
        url = requests.get(base_url, params = params)

    except Exception as e :
        print(f"Sorry! An Error appeared {e}")
        sys.exit()

    else :
        data = url.json()

        timelines = data["timelines"]["hourly"][0]["time"]
        temperature = data["timelines"]["hourly"][0]["values"]["temperature"]


        print(f"city : {city}")
        print(f"timelines : {timelines}")
        print(f"tempertaure : {temperature}")


        return




main()


