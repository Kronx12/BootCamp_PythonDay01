from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, pname):
        if not isinstance(pname, str) or str(pname) == "":
            print("Book creation error : Invalid Name")
            raise ValueError
        self.name = pname
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, pname):
        for r in self.recipes_list.get("starter"):
            if r.name == pname:
                return r
        for r in self.recipes_list.get("lunch"):
            if r.name == pname:
                return r
        for r in self.recipes_list.get("dessert"):
            if r.name == pname:
                return r
        return None

    def get_recipes_by_types(self, recipe_type):
        r_names = []
        for r in self.recipes_list.get(recipe_type):
            r_names.append(r.name)
        return r_names

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("recipe isn't a recipe!")
            raise ValueError
        self.last_update = datetime.now()
        all_r = []
        for r_name in self.get_recipes_by_types(recipe.recipe_type):
            all_r.append(self.get_recipe_by_name(r_name))
        all_r.append(recipe)
        self.recipes_list[recipe.recipe_type] = all_r
