import requests
from datetime import datetime

MY_LAT = 13.036711 # Your latitude
MY_LONG = 77.631826 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
# hour_now = int(str(time_now).split(" ")[1].split(":")[0])

if (abs(iss_latitude - MY_LAT)<=5) and (abs(iss_longitude - MY_LONG)<=5) and (hour_now>=sunset and hour_now<=sunrise):
    print("Look Above")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



