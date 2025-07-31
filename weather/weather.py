import requests


def get_weather(city):
    api_key = "gmvH4TaiHlYRF1WOzZpFfwDDVcg2aFvJ"
    base_url = "https://api.tomorrow.io/v4/weather/forecast"

    # Queries :
    params = {"location": city, "apikey": api_key, "timelines": "1h", "units": "metric"}

    # check if the city exists :
    with open("city.csv") as file:
        lines = [line.strip().split(",") for line in file]

        for i in range(len(lines)):
            if city in lines[i][0]:

                # request of accessing data / return in JSON format
                url = requests.get(base_url, params=params)

                # requests is succesful
                if url.status_code == 200:
                    # we transform the JSON format into dictionaries in python
                    data = url.json()

                    try:
                        time = data["timelines"]["hourly"][0]["time"]
                        temperature = data["timelines"]["hourly"][0]["values"][
                            "temperature"
                        ]

                        print(f"City  :  {city}")
                        print(f"Time  : {time}")
                        print(f"Temperature : {temperature}")

                    except KeyError:
                        print("missing keyword!!")

                else:
                    print(url.status_code)

            else:
                continue

        print("City Not Found")

    return


city = input("Enter city name : ")

get_weather(city)
