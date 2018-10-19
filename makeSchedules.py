from AgClass import *
from classScraper import *

def printHours(classes):
	for AgClass in classes:
		print(AgClass.subject, ' ', AgClass.section,' ', AgClass.printTime())

def makeSchedules(*classes):
	schedules = []
	newSchedules = []
	for AgClass in classes[0]:
		schedules.append(AgSchedule(AgClass))
	for AgClassList in classes[1:]:
		for AgClass in AgClassList:
			for schedule in schedules:
				if(schedule.canAddClass(AgClass)):
					x = AgSchedule(schedule.Classes.copy())
					x.addClass(AgClass)
					newSchedules.append(x)

		schedules = newSchedules.copy()
		newSchedules = []

	return AgScheduleList(schedules)

def viewSchedules(schedules):
	for y, x in enumerate(schedules):
		print('Schedule #',y+1)
		x.viewSchedule()


		
