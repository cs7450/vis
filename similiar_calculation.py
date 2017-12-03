import pandas as pd
import csv

data_input = pd.read_csv("recipes_ingredients_testing.csv", header = 0)
recipe_unique = list(set(data_input["recipe"]))
data_input.set_index("recipe", inplace = True)
row_list = []
for i in range(0, len(recipe_unique)):
	for j in range(0, len(recipe_unique)):
		if i != j:
			ingredient1 = data_input.loc[recipe_unique[i],"ingredient"]
			ingredient2 = data_input.loc[recipe_unique[j],"ingredient"]
			intersection = set(ingredient1).intersection(ingredient2)
			#print recipe_unique[i] + "\t" + recipe_unique[j] + "\t" + str(len(intersection))
			dict1 = {}
			dict1.update({"recipe1": recipe_unique[i],"recipe2": recipe_unique[j], "number": len(intersection)})
			row_list.append(dict1)
df = pd.DataFrame(row_list, columns = ["recipe1","recipe2","number"])
recipe_unique = list(set(df["recipe1"]))
df.set_index(["recipe1"], inplace = True)

dict_top10 = {}
for recipe in recipe_unique:
	df_new = pd.DataFrame(df.loc[recipe], columns = ["recipe1","recipe2","number"])
	df_new.sort_values(["number"],ascending=False, inplace = True)
	top10 = df_new.head(n = 10)["recipe2"].tolist()
	dict_top10.update({recipe:top10})

with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ingredient","intersection"])
    for key, value in dict_top10.items():
       writer.writerow([key, value])