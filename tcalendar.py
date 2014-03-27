'''
Created on 22.3.2014

@author: Olli Riikonen
'''

from event import Event
import calendar
import socket


class TCalendar(object):
    '''
    classdocs
    '''


    def __init__(self, name, colour, savefile=None):
        '''
        Constructor
        '''
        self.tcalendar = calendar.Calendar()
        self.events = []
        self.name = name
        self.colour = colour
        if not savefile:
            self.savefile = name+".ics"
        else:
            self.savefile = savefile
            #TODO: error handling/creating a new


    def add_event(self, event):
        '''
        Adds an event to the calendar
        '''
        self.events.append(event)
        self.events.sort()



    def delete_event(self, event):
        '''
        deletes the selected event from calendar
        '''
        self.events.remove(event)


    def load_events(self):
        '''
        Goes through the savefile to fetch all the calendars events.
        This is done for easier and more efficient editing of the calendar
        '''
        savefile = open(self.savefile, "r+", encoding="utf8")
        current_line = savefile.readline()

        while current_line != "END:VCALENDAR":
            if current_line == "BEGIN:VEVENT":
                event = Event()
                current_line = self.savefile.readline()

            while current_line != "END:VEVENT":
                event.add_attribute(current_line.split(':',1))

            current_line = self.savefile.readline()
            
        savefile.close()


    def save_events(self):
        '''
        Saves calendar for later use as .ics file
        '''
        savefile = open(self.savefile, "w", encoding="utf8")
        intro = ''.join(["BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//",socket.gethostname(),"//",self.name,"//EN\r\n"])
        savefile.write(intro)
        for event in self.events:
            savefile.write("BEGIN:VEVENT\r\n")
            events_attributes = event.get_attributes()
            for att in events_attributes:
                savefile.write(''.join([att,":", events_attributes[att],"\r\n"]))
            savefile.write("END:VEVENT\r\n")
            
        savefile.write("END:VCALENDAR")
            
        savefile.close()

    def get_visible_events(self, start, end):
        '''
        Returns all the events that are visible in selected calendar view
        '''
        visible = []
        for event in self.events:
            print(event.get_start())
            if event.get_start() >= start:
                visible.append(event)
            elif event.get_start() >= end:
                break
        return visible
