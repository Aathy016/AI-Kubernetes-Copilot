import json
import os
from datetime import datetime


class TimelineManager:

    def __init__(self):

        self.timeline_file = (
            "storage/timeline.json"
        )


    def create_event(
        self,
        title,
        description
    ):

        events = self.get_events()


        event = {

            "timestamp":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "title": title,

            "description": description
        }


        events.append(event)


        with open(
            self.timeline_file,
            "w"
        ) as file:

            json.dump(
                events,
                file,
                indent=4
            )


    def get_events(self):

        if not os.path.exists(
            self.timeline_file
        ):

            return []


        with open(
            self.timeline_file,
            "r"
        ) as file:

            return json.load(file)