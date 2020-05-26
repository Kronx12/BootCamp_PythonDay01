from book import Book
from recipe import Recipe
from time import sleep

livre = Book("Book1")
print("Creation date : ", livre.creation_date)
print("Last Update : ", livre.last_update)
sleep(5)

recipe = Recipe("puree", 1, 15, ["patates"],
                "Puree de patates", "lunch")
recipe2 = Recipe("choucroutte", 2, 120, ["patates", "choux"],
                 "Choucroutte light", "starter")

livre.add_recipe(recipe)
livre.add_recipe(recipe2)

for i in livre.get_recipes_by_types("starter"):
    print(livre.get_recipe_by_name(i))
for i in livre.get_recipes_by_types("lunch"):
    print(livre.get_recipe_by_name(i))

print("Creation date : ", livre.creation_date)
print("Last Update : ", livre.last_update)
