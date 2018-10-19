import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
from AgClass import *

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

baseURL = 'https://compass-ssb.tamu.edu/pls/PROD/bwckschd.p_get_crse_unsec?sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_title=&sel_schd=%25&sel_insm=%25&sel_from_cred=&sel_to_cred=&sel_camp=%25&sel_levl=%25&sel_ptrm=%25&sel_instr=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&'


def stringHoursToArray(date):
	#String will always be in '9:10 am - 10:00 am' format.
	split = date.split(' ')
	startTime = split[0].split(':')
	endTime = split[3].split(':')
	startTime = [int(i) for i in startTime]
	endTime = [int(i) for i in endTime]


	if startTime[0] == 12:
		startTime[0] = 0
	if endTime[0] == 12:
		endTime[0] = 0

	if split[1] == 'pm':
		startTime[0] += 12
	if split[4] == 'pm':
		endTime[0] += 12

	hours = [startTime[0] * 60 + startTime[1], endTime[0]* 60 + startTime[1]]

	return hours




def getClasses(year, semester, subject, course):
	
	dayToIndex = {'M':0, 'T':1, 'W':2, 'R':3, 'F':4}

	termData = year * 100 + 31 if semester == 'Fall' else year*100+11 #Term is 201831 for Fall 2018 and 201911 for Spring 2019
	
	newData = {'term_in': termData, 'sel_subj':subject,'sel_crse':course}



	urlData = urllib.parse.urlencode(newData)
	newURL = baseURL + urlData


	request = urllib.request.Request(url=newURL) #User-agent python does not work
	request.remove_header('User-agent')
	request.add_header('User-agent','Mozilla/5.0')
	
	page = urllib.request.urlopen(request, context=context)

	soup = BeautifulSoup(page, 'html.parser')
	AgClasses = []
	for x in soup.find_all('th', 'ddtitle'):
		section = x.a.text[-3:] #Parse for section
		#soup.th.parent.next_sibling.next_sibling.table #Oarse for times
		hours = [[0,0]] * 5 
		for y in x.parent.next_sibling.next_sibling.table.find_all('tr'):
			if(y.td is not None):
				if(y.td.text == 'Lecture' or y.td.text == 'Laboratory'):
					currHours = stringHoursToArray(y.td.next_sibling.next_sibling.text)
					days = y.td.next_sibling.next_sibling.next_sibling.next_sibling.text
					for z in days:
						hours[dayToIndex[z]] = currHours

		AgClasses.append(AgClass(subject+str(course), section, hours))




	return AgClasses


