from AgClass import *
from classScraper import *

ChemClasses = [AgClass('CHEM107', '501', [[550,600],[0,0],[550,600],[0,0],[550,600]]), AgClass('CHEM107', '502', [[690,740],[0,0],[690,740],[0,0],[690,740]])]
EngrClasses = [AgClass('ENGR111', '504',[[610,690],[0,0],[610,690],[0,0],[610,660]])]
MathClasses = [AgClass('MATH150', '507', [[760,810],[860,935],[0,0],[860,935],[0,0]]), AgClass('MATH150', '502', [[0,0],[765,840],[480,530],[765,840],[0,0]])] 
ChemLabClasses = [AgClass('CHEM117', '501', [[480,650],[0,0],[0,0],[0,0],[0,0]]), AgClass('CHEM117', '505', [[690,860],[0,0],[0,0],[0,0],[0,0]]), AgClass('CHEM117', '507', [[900,1070],[0,0],[0,0],[0,0],[0,0]]), AgClass('CHEM117', '525', [[0,0],[0,0],[480,650],[0,0],[0,0]]), AgClass('CHEM117', '528', [[0,0],[0,0],[690,860],[0,0],[0,0]]), AgClass('CHEM117', '522', [[0,0],[1110,1280],[0,0],[0,0],[0,0]])]
PolsClasses = [AgClass('POLS206', '503', [[1065,1140],[0,0],[1065,1140],[0,0],[0,0]]), AgClass('POLS206', ' 501', [[0,0],[765,840],[0,0],[765,840],[0,0]]), AgClass('POLS206', ' 504', [[0,0],[860,935],[0,0],[860,935],[0,0]]), AgClass('POLS206', ' 505', [[970,1045],[0,0],[970,1045],[0,0],[0,0]]), AgClass('POLS206', ' 506', [[0,0],[670,745],[0,0],[670,745],[0,0]]), AgClass('POLS206', ' 508', [[0,0],[765,840],[0,0],[765,840],[0,0]])]

def printHours(classes):
	for AgClass in classes:
		print(AgClass.subject, ' ', AgClass.section,' ', AgClass.printTime())

def makeSchedules(*classes):
	schedules = []
	newSchedules = []
	for AgClass in classes[0]:
		schedules.append(AgSchedule(AgClass))
	comparisons = 0
	for AgClassList in classes[1:]:
		for AgClass in AgClassList:
			for schedule in schedules:
				comparisons += 1
				if(schedule.canAddClass(AgClass)):
					x = AgSchedule(schedule.Classes.copy())
					x.addClass(AgClass)
					newSchedules.append(x)

		schedules = newSchedules.copy()
		newSchedules = []

	print(comparisons)
	return AgScheduleList(schedules)

def viewSchedules(schedules):
	for y, x in enumerate(schedules):
		print('Schedule #',y+1)
		x.viewSchedule()


		
