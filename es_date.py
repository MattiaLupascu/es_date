import datetime
data=datetime.datetime.now()
#1
print(data)

data=datetime.datetime(2006,11,17)
#2
print(data.strftime("%c"))
#3
print(data)
#4
print(data.strftime("%A" +"%B"+"%Y"))