# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in list(data)[1:]:
#         temperature.append(int(row[1]))
#
# print(temperature)
import numpy
import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# avr_temp = numpy.average(temp_list)
# print(avr_temp)
# avr_temp2 = data["temp"].mean()
# print(avr_temp2)
# max_val = data["temp"].max()
# # print(max_val)
#
# print(data[data.temp == max_val])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
monday_temp_f = (monday_temp * 1.8) + 32
print(monday_temp_f)

# data_dict = {
#     "students": ["Ania", "Ola", "Pawel"],
#     "scores": [15, 14, 13]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data_csv.txt")

# data = pandas.read_csv("Squirrel_Data.csv")
# cinnamon_fur_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray_fur_color = len(data[data["Primary Fur Color"] == "Gray"])
# black_fur_color = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["cinnamon", "gray", "black"],
#     "Count": [cinnamon_fur_color, gray_fur_color, black_fur_color]
# }
# data_new = pandas.DataFrame(data_dict)
# data_new.to_csv("squirrel_fur.csv")