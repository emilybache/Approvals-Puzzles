import random
import logging


def init_logging():
    # create logger on the current module and set its level
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)

    # create a formatter that creates a single line of json with a comma at the end
    formatter = logging.Formatter(
        (
            '{"unix_time":%(created)s, "time":"%(asctime)s", "module":"%(name)s",'
            ' "level":"%(levelname)s", "msg":"%(message)s"},'
        )
    )

    # create a channel for handling the logger and set its format
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # connect the logger to the channel
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    # send an example message
    logger.info('logging is working')
    return logger


questions = {"The world is flat" : False,
             "The moon is made of cheese" : False,
             "Antarctica is colder on average than Africa": True,
             "Jupiter is the biggest planet in the solar system": True,
             "The longest river on Earth is the Nile": True,
             "Gambia is in South America": False,
             "Mt Everest is the highest mountain in the world": True,
             }


def main():
    logger = init_logging()
    for q, a in questions.items():
        logger.info("asking question '%s'", q)
        response = input(q + "\nTrue or False?\n")
        if response.upper() == "TRUE" or response.upper() == "T":
            b = True
        elif response.upper() == "FALSE" or response.upper() == "F":
            b = False
        else:
            b = bool(response)
        if b == a:
            logger.info("CORRECT")
            print("Correct!")
        else:
            logger.info("INCORRECT")
            print("No, sorry")


if __name__ == "__main__":
    main()