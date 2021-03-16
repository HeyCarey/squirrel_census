import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])

black = len(squirrel[squirrel["Primary Fur Color"] == "Black"])

cinnamon = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])

print(gray)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_by_color.csv")