import forecastio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


api_key = "cb91f1d7b02d54aa27438663b43dee23"
lat = 37.967819
lng = 112.87718
forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.hourly()
#print(byHour.summary)
#print(byHour.icon)
a = []
for hourlyData in byHour.data:
    a.append(hourlyData.temperature)
    #print(hourlyData.temperature)

x = list(range(49))
y = a
plt.plot(x,y)
plt.xlabel('hour')
plt.ylabel('Celsius')
plt.title('The temperature in the next 48 hours from now')
plt.yticks([15, 19, 23, 27, 31])
plt.grid(True)
#plt.show()
plt.savefig("./Figure_1.png")

