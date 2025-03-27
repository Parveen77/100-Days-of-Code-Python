import pandas

#data = pandas.read_csv("abc.csv")
#day = data[data["day"] == "monday"]
#print(day)

data = pandas.read_csv("Squirrel_Data.csv")

fur_color_gray = len(data[data["Primary Fur Color"] == "Gray"])
print(fur_color_gray)

fur_color_black = len(data[data["Primary Fur Color"] == "Black"])
print(fur_color_black)

fur_color_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(fur_color_cinnamon)

dict = { 
        "fur_color": ["gray", "black", "cinnamon"],
        "count":[fur_color_gray, fur_color_black, fur_color_cinnamon]
    }

df = pandas.DataFrame(dict)
df.to_csv("squirrel_count.csv")

