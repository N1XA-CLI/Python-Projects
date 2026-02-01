# import csv
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
# pandas.DataFrame.to_excel(report, excel_writer="weather_report.xlsx")
temp_list = report["temp"]
# print(f"Max Temperature: {temp_list.max()}")
# avg_temp = sum(temp_list) / len(temp_list)
# avg_temp = report["temp"].mean()
# print(f"Average Temperature: {avg_temp}")
print(report[report.day == "Monday"])
print(report[report.temp == temp_list.max()])
# monday = report[report.day == "Monday"]
# print(monday.temp * 1.8 + 32)

# dict_data = {
#     "students": ["Amy", "N1XA", "Angela"],
#     "score": [75, 23, 86]
# }

# print(dict_data)
# data = pandas.DataFrame(dict_data)
# data.to_csv("new_data.csv")
# print(data)

# import pandas
# Main Work

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)
#
# data_color_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
#
# df = pandas.DataFrame(data_color_dict)
# df.to_csv("squirrel_count.csv")