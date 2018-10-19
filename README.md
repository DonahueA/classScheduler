# classScheduler

With this python script you can easily determine your schedule for any semester. Classes schedules are scraped from the web then used to create a schedule.

This was a small project I developed for personal use.

# Usage

run makeSchedules.py in interactive mode
```
python3 -i makeSchedules.py 
```
Then use getClasses(year, Semester, Subject, Course) to get a list of all the classes for that course.
```
mathClasses = getClasses(2018, 'Spring', 'MATH', 150)
chemClasses = getClasses(2018, 'Spring', 'CHEM', 107)
```

if you want to see the available times for a class:
```
printHours(chemClasses)
CHEM107   501   M: 09:10-10:10 T:             W: 09:10-10:10 TH:             F: 09:10-10:10
CHEM107   502   M: 11:30-12:30 T:             W: 11:30-12:30 TH:             F: 11:30-12:30
CHEM107   M01   M:             T: 08:00-09:00 W:             TH: 08:00-09:00 F:            
```
Create a schedule of any number of classes
```
allSchedules = makeSchedules(mathClasses, chemClasses)
```

```
allSchedules.count()
35
```
You can choose to see only the schedules with a specific section with
```
allSchedules.selectClass('MATH150', '507')
```

now allSchedule.viewSchedule() shows all course combinations with MATH 150-507
```
allSchedules.viewSchedules()
Schedule # 1
MATH150 507   M: 12:40-13:40 T: 14:20-15:20 W:             TH: 14:20-15:20 F:            
CHEM107 501   M: 09:10-10:10 T:             W: 09:10-10:10 TH:             F: 09:10-10:10


Schedule # 2
MATH150 507   M: 12:40-13:40 T: 14:20-15:20 W:             TH: 14:20-15:20 F:            
CHEM107 502   M: 11:30-12:30 T:             W: 11:30-12:30 TH:             F: 11:30-12:30


Schedule # 3
MATH150 507   M: 12:40-13:40 T: 14:20-15:20 W:             TH: 14:20-15:20 F:            
CHEM107 M01   M:             T: 08:00-09:00 W:             TH: 08:00-09:00 F:  
```

and hide schedules with sections you don't want to take.
```
allSchedules.hideClass('CHEM107', 'M01')
allSchedules.viewSchedules()
Schedule # 1
MATH150 507   M: 12:40-13:40 T: 14:20-15:20 W:             TH: 14:20-15:20 F:            
CHEM107 501   M: 09:10-10:10 T:             W: 09:10-10:10 TH:             F: 09:10-10:10


Schedule # 2
MATH150 507   M: 12:40-13:40 T: 14:20-15:20 W:             TH: 14:20-15:20 F:            
CHEM107 502   M: 11:30-12:30 T:             W: 11:30-12:30 TH:             F: 11:30-12:30
```


