import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from storage.timeline_manager import TimelineManager


timeline = TimelineManager()


timeline.create_event(
    "TEST EVENT",
    "Timeline module working"
)


events = timeline.get_events()


print(events)