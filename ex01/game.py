class GotCharacter:
    def __init__(self, pfirst_name, pis_alive=True):
        if not isinstance(pfirst_name, str) or pfirst_name == "":
            print("Erreur GotCharacter: Invalid first_name")
            raise ValueError
        self.first_name = pfirst_name
        self.is_alive = True

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, pfirst_name, pis_alive=True):
        super().__init__(pfirst_name, pis_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False