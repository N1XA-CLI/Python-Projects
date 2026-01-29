import csv
import pandas

# with open("weather_data.csv") as weather_report:
#     weekly_report = csv.reader(weather_report)
#     tempratures = []
#     for day_report in weekly_report:
#         if day_report[1] != "temp":
#             tempratures.append(int(day_report[1]))
#     print(tempratures)

report = pandas.read_csv("weather_data.csv")
print(report["temp"])
    