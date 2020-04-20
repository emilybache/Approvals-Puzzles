#/usr/bin/env python3

import random
import time

responses = ["ROFL!",
             "LOL",
             "Chuckle",
             "That's an old one!",
             "I think I heard that one before",
             "Ha ha",
             "Really?",
             "Groan...",
             "Yeah whatever...",
             "I can't take much more of this",
             "I feel sick",
             "please kill me now",
             ]

dad_jokes = ["How do you make holy water? You boil the hell out of it.",
             "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!",
             "What do you call someone with no body and no nose? Nobody knows.",
             "What is the least spoken language in the world? Sign language",
             "Spring is here! I got so excited I wet my plants!",
             "Don't trust atoms. They make up everything!",
             "Why did the invisible man turn down the job offer? He couldn't see himself doing it.",
             "CASHIER: 'Would you like the milk in a bag, sir?' DAD: 'No, just leave it in the carton!'",
             "What do you call a dog that can do magic? A Labracadabrador.",
             "What do you call a deer with no eyes? No idea!",
             "When a dad drives past a cow pasture: LOOK! That cow is OUT-STANDING in his field!",
             "When you ask a dad if he's alright: 'No, I'm half left.'",
             ]


def main(sleeptime):
    for response in responses:
        joke_nr = random.randint(0, len(dad_jokes)-1)
        joke = dad_jokes[joke_nr]
        print(f"DAD: {joke}")
        time.sleep(sleeptime)
        del dad_jokes[joke_nr]
        print(f"ME: {response}")
        time.sleep(sleeptime)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sleeptime = int(sys.argv[1])
    else:
        sleeptime = 2
    main(sleeptime)