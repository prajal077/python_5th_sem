# polymorphism

class Cat :
    def speak(self) :
        print("cat meows")

class Dog :
    def speak(self) :
        print("Dog Barks")

obj = [Cat(), Dog()]

for i in obj :
    i.speak()

# exceptional handling

try :
    print(x)
except Exception as e :
    print("error")
else :
    print("not error")
finally :
    print("This is finally block")


try :
    a
except NameError as e :
    print("Name error")
else :
    print("not error")

# API fetching

import requests

def get_weather(city):
    api_key = "8d72acc22cbc5f84fb1eb190deb7e2d9"  # Replace with a new API key
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if "error" in data:
            print(f"Error: {data['error']['message']}")
        else:
            location = data['location']['name']
            temp = data['current']['temp_c']

            print(f"Location: {location}")
            print(f"Temperature: {temp}°C")
    else:
        print("Error fetching data")

try:
    city = input("Enter city name: ")
    get_weather(city)
except Exception as e:
    print("Error:", e)


