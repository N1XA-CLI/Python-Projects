import pandas

with open("weather_data.csv") as weather_report:
    reports = [report.strip() for report in weather_report.readlines()]
    print(reports)
    