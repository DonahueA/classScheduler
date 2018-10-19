class AgClass:
	def __init__(self, subject, section, hours):
		self.subject = subject
		self.section = section
		self.hours = hours
	def hasConflict(self, AgClass2):
		for x in range(len(self.hours)):
			if(self.hours[x][0] < AgClass2.hours[x][1] and AgClass2.hours[x][0] < self.hours[x][1]):
				return True
		return False

	def printTime(self):
		def timeToString(time):
			if(time[0] == time[1]):
				return "           "
			return '{:02}:{:02}-{:02}:{:02}'.format(time[0]//60,time[0]%60,time[1]//60,time[1]%60)

		return "M: "+ timeToString(self.hours[0]) + " T: "+timeToString(self.hours[1])  + " W: "+timeToString(self.hours[2]) + " TH: "+timeToString(self.hours[3]) + " F: "+timeToString(self.hours[4]) 

		
class AgSchedule:
	def __init__(self, AgClass):
		if(isinstance(AgClass, list)):
			self.Classes = AgClass
		else:
			self.Classes = [AgClass]

	def hasClass(self, subject, section):
		for AgClass in self.Classes:
			if AgClass.section == section and AgClass.subject == subject:
				return True

	def addClass(self, AgClass):
		if(self.canAddClass(AgClass)):
			self.Classes.append(AgClass)

	def copy(self):
		return AgSchedule(self.Classes.copy)

	def canAddClass(self, newAgClass):
		for AgClass in self.Classes:
			if(AgClass.hasConflict(newAgClass)):
				return False
		return True

	def viewSchedule(self):
		for AgClass in self.Classes:
			print(AgClass.subject, AgClass.section, ' ', AgClass.printTime())
		print('\n')

class AgScheduleList:
	def __init__(self, AgScheduleList):
		self.ScheduleList = AgScheduleList
		self.selectedClasses = []
		self.hiddenClasses = []

	def count(self):
		filteredList = self.ScheduleList
		for subject, section in self.selectedClasses:
			filteredList = [schedule for schedule in filteredList if schedule.hasClass(subject, section)]
		for subject, section in self.hiddenClasses:
			filteredList = [schedule for schedule in filteredList if not schedule.hasClass(subject, section)]
		return len(filteredList)

	def viewSchedules(self):
		filteredList = self.ScheduleList
		for subject, section in self.selectedClasses:
			filteredList = [schedule for schedule in filteredList if schedule.hasClass(subject, section)]
		for subject, section in self.hiddenClasses:
			filteredList = [schedule for schedule in filteredList if not schedule.hasClass(subject, section)]

		for y, x in enumerate(filteredList):
			print('Schedule #',y+1)
			x.viewSchedule()

	def selectClass(self, subject, section):
		self.selectedClasses.append((subject, section))

	def deselectClass(self, subject, section):
		self.selectedClasses.remove((subject, section))

	def viewSelectedClasses(self):
		for subject, section in self.selectedClasses:
			print(subject, ' ', section)

	def hideClass(self, subject, section):
		self.hiddenClasses.append((subject, section))

	def unhideClass(self, subject, section):
		self.hiddenClasses.remove((subject, section))
	
	def viewHiddenClasses(self):
		for subject, section in self.selectedClasses:
			print(subject, section)


