import random

questions = {"The world is flat" : False,
             "The moon is made of cheese" : False,
             "Antarctica is colder on average than Africa": True,
             "Jupiter is the biggest planet in the solar system": True,
             "The longest river on Earth is the Nile": True,
             "Gambia is in South America": False,
             "Mt Everest is the highest mountain in the world": True,
             }


def main():
    for q, a in questions.items():
        response = input(q + "\nTrue or False?\n")
        if response.upper() == "TRUE" or response.upper() == "T":
            b = True
        elif response.upper() == "FALSE" or response.upper() == "F":
            b = False
        else:
            b = bool(response)
        if b == a:
            print("Correct!")
        else:
            print("No, sorry")

if __name__ == "__main__":
    main()