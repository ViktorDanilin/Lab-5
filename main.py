# вариант 4
import requests
import json

# newsapi
url_1 = ('https://newsapi.org/v2/everything?'
         'q=Apple&'
         'from=2022-09-22&'
         'sortBy=popularity&'
         'apiKey=694c15265e8c435fbc7d9e827ca5e917')

r_1 = requests.get(url_1)
r_1 = r_1.json()
with open('requests_1.json', 'w') as file_1:
    json.dump(r_1, file_1, indent=3)

# current weather on Novosibirsk
# for Novosibirsk lat=55.018803, lon=82.933952
url_2 = ('http://api.openweathermap.org/data/2.5/weather?'
         'lat=55.01&'
         'lon=82.93&'
         'appid=7cdcfaa69a322e2c77fdf3043de45290&'
         'units=metric&'
         'lang=ru')
res = requests.get(url_2)
data = res.json()
print("погода в Новосибирске:", data['weather'][0]['description'])
print("температура:", data['main']['temp'], "по Цельсию")
print("давление:", data['main']['pressure'], "гекто-паскаль")
print("влажность:", data['main']['humidity'], "%")
