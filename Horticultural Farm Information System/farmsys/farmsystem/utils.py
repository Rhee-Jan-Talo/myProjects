
from django.db.models import Q
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from .models import user_account

import datetime
from datetime import date
from datetime import datetime,timedelta

#import MySQLdb
import mysql.connector
import re
import os

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, batch_id=None):
		self.year = year
		self.month = month
		self.batch_id = batch_id
		super(Calendar, self).__init__()
		self.save_data()

	# formats a day as a td
	# filter events by day
	

	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		#events_per_day = self.fetch_data(f'select * from plant_monitoring where batch_id = {self.batch_id} and plant_monitoring.date_from >= {self.year}-{self.month}-{day};')


		d = ''
		for event in events_per_day:
			d += f'<p><b>Plant Stage</b>: {event.plant_stage}<br><b>Activity</b>: {event.activity}<br><b>Description</b>: {event.description}<br><b>Remarks</b>: {event.remarks}</p><hr>' #putting the event title

		if day != 0:
			return f"<td><span class='date'>{day}.)</span><ul> {d} </ul></td>" #selecting the event date
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month, batch_id = self.batch_id)



		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal


	def save_data(self):
		events = self.fetch_data(f'select plant_monitoring.*, plant_activities.activity, plant_activities.report from plant_monitoring left join plant_activities on plant_monitoring.activities_id = plant_activities.activities_id where batch_id = {self.batch_id};')
		
		for data in events:
			try:
				ev = Event.objects.get(
					Q(description = data['report']), Q(activity = data['activity']),
					Q(activities_id = data['activities_id'])
					)
			except Event.DoesNotExist:
				create = Event.objects.create(
					activities_id = data['activities_id'],
					batch_id = data['batch_id'],
					plant_stage = data['plant_stage'],
					activity = data['activity'],
					description = data['report'],
					start_time = data['date_from'],
					end_time = data['date_to'],
					remarks = data['remarks'],
					)






	def fetch_data(self,query):
	    mydb = mysql.connector.connect(
	       host ="localhost",
	       user="root",
	       password="root",
	       database="farmsys",


	       )
	    mycursor = mydb.cursor(dictionary=True)
	    mycursor.execute(query)
	    myresult = mycursor.fetchall()
	    return myresult 




'''

from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from .models import user_account

import datetime
from datetime import date
from datetime import datetime,timedelta

#import MySQLdb
import mysql.connector
import re
import os

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, batch_id = None):
		self.year = year
		self.month = month
		self.batch_id = batch_id
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)

		d = ''
		for event in events_per_day:
			d += f'<p><b>{event.title}</b></p>' #putting the event title

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>" #selecting the event date
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal

	def fetch_data(query):
	    mydb = mysql.connector.connect(
	       host ="localhost",
	       user="root",
	       password="rheejantalo",
	       database="farmsys",


	       )
	    mycursor = mydb.cursor(dictionary=True)
	    mycursor.execute(query)
	    myresult = mycursor.fetchall()
	    return myresult 


'''