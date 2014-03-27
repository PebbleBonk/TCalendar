import unittest
import datetime
from event import Event
from tcalendar import TCalendar
from corrupted_savefile_error import CorruptedSavefileError







class Test(unittest.TestCase):

    def test_simple_cal_and_event(self):

        cal = TCalendar("test", "green")
        ev = Event()
        ev1 = Event()
        ev2 = Event()

        ev.add_attribute(["DTSTAMP", "20140422T123456Z"])
        ev.add_attribute(["UID", "uid@examp.le"])
        ev.add_attribute(["SUMMARY", "foofooandfoo foo"])

        ev1.add_attribute(["DTSTAMP", "20140424T050000Z"])
        ev1.add_attribute(["SUMMARY", "second event"])

        ev2.add_attribute(["DTSTAMP", "20140418T101500Z"])
        ev2.add_attribute(["SUMMARY", "and third example"])

        cal.add_event(ev)
        cal.add_event(ev1)
        cal.add_event(ev2)

        
        dateEnd = datetime.datetime(2014, 4, 21, 0, 0, 0)
        dateStart = datetime.datetime(2014, 4, 21, 0, 0, 0)


        self.assertEqual("20140422T123456Z", ev.get_attribute("DTSTAMP"), "datestramp not saved properly")
        self.assertEqual([ev, ev1], cal.get_visible_events(dateStart, dateEnd), "Wrong events fetched from tcalendar")

        cal.save_events()



        #add event
        #add event
        #get event
        #get tcalendar

        #Check: no errors, right attribute (random)


    #test load tcalendar
        #load tcalendar
        #check tcalendar by get attribute/event

        #test copy-paste