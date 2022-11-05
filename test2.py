from praw.reddit import Reddit
from praw.models import Message
import random

import logging

def poll_inbox_stream(instance: Reddit):
    for praw_thing in instance.inbox.stream(pause_after=0):
        if isinstance(praw_thing, Message):
            print("found a message")
        else:
            print(f"found something else {type(praw_thing)}")
        if praw_thing is None:
            break

        record = None

        if not record:
            print("record is None")
            continue


if __name__ == '__main__':
    instance: Reddit = Reddit(site_name="Pablobot-GPT2")
    while True:
        poll_inbox_stream(instance)




