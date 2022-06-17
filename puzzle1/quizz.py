#!/usr/bin/env python

import random
import logging


def init_logging():
    # create logger on the current module and set its level
    logger = logging.getLogger("quizz")
    logger.setLevel(logging.INFO)

    # create a formatter that creates a single line of json
    formatter = logging.Formatter(
        (
            '{"unix_time":%(created)s, "time":"%(asctime)s", "module":"%(name)s",'
            ' "level":"%(levelname)s", "msg":"%(message)s"}'
        )
    )

    # create a channel for handling the logger and set its format
    ch = logging.FileHandler("quizz.log")
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
             "The longest river on Earth is the Nile or the Amazon": True,
             "Gambia is in South America": False,
             "Mt Everest is the highest mountain in the world": True,
             }


def main():
    logger = init_logging()
    for q, a in questions.items():
        logger.info("asking question '%s'", q)
        response = input(q + "\nTrue or False? (please write your answer as T or F)\n")
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