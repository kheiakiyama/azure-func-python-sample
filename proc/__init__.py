import logging

import azure.functions as func
import json


def main(event: func.EventGridEvent, outputblob: func.Out[func.InputStream]):
    logging.info("Python Event Grid function processed a request.")
    logging.info("  Subject: %s", event.subject)
    logging.info("  Time: %s", event.event_time)
    logging.info("  Data: %s", event.get_json())

    outputblob.set(event.get_json())
