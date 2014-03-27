from event import Event
from calendar import Calendar
from corrupted_savefile_error import CorruptedSavefileError

class UIdummy(object):

    def __init__(self):
        self.calendars = []

    def load_cal(self, filename, name, color):
        self.calendars.append(Calendar(name, color, filename))
        return self.calendars[-1]

    def new_cal(self, name, color):
        self.calendars.append(Calendar(name, color))
        return self.calendars[-1]

    def get_cal(self):
        pass
    