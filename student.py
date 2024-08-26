from datetime import date, timedelta
import requests

class Student:
    """ A student class as base for method testing """

    def __init__(self, first_name, last_name):
        """  the _ at start denotes read only """
        self._first_name = first_name
        self._last_name = last_name
        """ create a start date from when the first instance of the student is created """
        self._start_date = date.today()
        """ create an end date (editable) as fictional course is one year long """
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    
    """ method to get data only (read only) so can use @property decorator"""
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
    

    def alert_santa(self):
        self.naughty_list = True
    

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)


    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"