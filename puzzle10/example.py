#!/usr/bin/env python
import logging, sys, os, time

def init_logging():
    # create logger on the current module and set its level
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        (
            '%(asctime)s %(message)s'
        )
    )

    # create a channel for handling the logger and set its format
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)

    # connect the logger to the channel
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    return logger


if __name__ == "__main__":
    logger = init_logging()

    logger.info("Initializing AcmeDB ...")
    time.sleep(0.25)
    logger.info("Setting up x y and z")
    time.sleep(0.25)
    logger.info("Running self checks")
    time.sleep(0.1)
    logger.info("AcmeDB Started! process_id=%s" % os.getpid())
    logger.info("Ready to accept connections")

