'''
Created on 22.3.2014

@author: Olli Riikonen
'''
from corrupted_savefile_error import CorruptedSavefileError
import datetime

class Event(object):
    '''
    A class to handle the tcalendar's events. Stores the attributes in a list
    TODO: maybe a dict for different icalendar -based attributes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        self.attributes = {}

    def get_start(self):
        if "DTSTART" not in self.attributes:
            return self.get_date()
        else:
            return self.convert_date(self.attributes["DTSTART"])

    def get_date(self):
        '''
        Returns the event's date as a datetime object
        '''
        return self.convert_date(self.attributes["DTSTAMP"])

    def add_attribute(self, att):
        '''
        Adds an attribute to the event.
        Input is a tuple with tag first and data second
        Attributes are stored in a dictionary for easy access
        '''
        if len(att) != 2:
            raise CorruptedSavefileError("invalid attribute syntax")
        self.attributes[att[0]] = att[1]

    def remove_attribute(self, att):
        '''
        Deletes an attribute from the event
        This can happen if information is set empty as an event is modified
        '''
        self.attributes.pop(att)

    def get_attribute(self, att):
        '''
        Returns wanted attribute for e.g. printing
        '''
        return self.attributes[att]
    
    def get_attributes(self):
        '''
        Returns all the event's attributes for e.g. saving
        '''
        return self.attributes

    def convert_date(self, date_string):
        '''
        Converts the dateformat used in .ics -files to Python's datetime object
        '''
        #TODO: strip 0:s and utilize timezone
        
        date_string = date_string[:-1].split('T')
        year = int(date_string[0][0:4])
        month = int(date_string[0][4:6])
        day = int(date_string[0][6:8])

        hour = int(date_string[1][0:2])
        minute = int(date_string[1][2:4])
        second = int(date_string[1][4:6])

        return datetime.datetime(year, month, day, hour, minute, second)

    def __le__(self, other):
        '''
        Overloads the >= operator for easy sorting in tcalendar class.
        Works based on the datestamp of the event
        '''
        return self.get_date() <= other.get_date()

    def __lt__(self, other):
        '''
        Overloads the > operator for easy sorting in tcalendar class.
        Works based on the datestamp of the event
        '''
        return self.get_date() < other.get_date()

