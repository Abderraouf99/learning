import pandas

data = pandas.read_csv("nyc_squirl_data.csv")


def get_animal_color_count(row, color):
    animal_color = row.where(row == color)
    return animal_color.count()


# removing the missing values
if data["Primary Fur Color"].isna:
    data["Primary Fur Color"].dropna()

grey_color_count = get_animal_color_count(data["Primary Fur Color"], "Gray")
cinnamon_color_count = get_animal_color_count(data["Primary Fur Color"], "Cinnamon")
black_color_count = get_animal_color_count(data["Primary Fur Color"], "Black")

data_dict = {"Fur color": ["Gray", "Cinnamon", "Black"], "count": [grey_color_count, cinnamon_color_count, black_color_count]}
result_df = pandas.DataFrame(data_dict).to_csv("result.csv", index=False)
