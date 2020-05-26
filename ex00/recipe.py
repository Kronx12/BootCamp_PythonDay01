class Recipe:
    def __init__(self, pname, pcooking_level, pcooking_time,
                 pingredients, pdescription, precipe_type):
        if not isinstance(pname, str) or str(pname) == "":
            print("Recipe creation error : Invalid Name")
            raise ValueError
        self.name = str(pname)
        if not isinstance(pcooking_level, int):
            print("Recipe creation error : Invalid Cooking Level")
            raise ValueError
        if pcooking_level < 1 or pcooking_level > 5:
            print("Recipe creation error : Invalid Cooking Level")
            raise ValueError
        try:
            self.coocking_level = int(pcooking_level)
        except ValueError:
            raise ValueError
        if not isinstance(pcooking_time, int):
            print("Recipe creation error : Invalid Cooking Time")
            raise ValueError
        try:
            self.cooking_time = int(pcooking_time)
        except ValueError:
            raise ValueError
        if not isinstance(pingredients, list):
            print("Recipe creation error : Invalid Ingedients")
            raise ValueError
        try:
            self.ingredients = list(pingredients)
        except ValueError:
            raise ValueError
        self.description = str(pdescription)
        if precipe_type != "starter":
            if precipe_type != "lunch":
                if precipe_type != "dessert":
                    print("Recipe creation error : Invalid Recipe type")
                    raise ValueError
        self.recipe_type = str(precipe_type)

    def __str__(self):
        txt = ""
        txt = self.name + " : "
        txt += "level=" + str(self.coocking_level) + " "
        txt += "time=" + str(self.cooking_time) + " "
        txt += "ingredients=" + str(self.ingredients) + " "
        txt += "description=" + str(self.description) + " "
        txt += "type=" + str(self.recipe_type)
        return txt
