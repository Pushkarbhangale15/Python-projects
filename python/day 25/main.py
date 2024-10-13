# # # with open("./weather_data.csv") as file:
# # #     data=file.readlines()
# # #     print(data)
# # import csv
# # with open("./weather_data.csv") as file:
# # 	data=csv.reader(file)
# # 	temperatures=[]
	
# # 	for row in data:
# # 		if row[1]!="temp":
# # 			temperatures.append(int(row[1]))
# # 	print(temperatures)
# import pandas as pd
# import math
# data =pd.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dict=data.to_dict()
# # print(data_dict)

# # print(data["temp"].mean())
# # print(data["temp"].max())
# monday=data[data.day=="Monday"]
# monday_temp_f=(monday.temp*9/5+32)
# print(monday_temp_f)
# #create a 
import pandas as pd
data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(gray_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)
data_dict={
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}
pd.DataFrame(data_dict).to_csv("squirrel_count.csv")



