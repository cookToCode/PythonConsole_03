#cookToCode


#A.) This is a program is designed to convert TB to GB and calculate
#the time it takes to fill a storage drive with a set amount of bytes

#This is my variable library. I will be reassigning varibles to streamline this program
freeSpace = float(0.0)
spaceUsed = 0
spaceUsedDaily = 0 
daysLeft = 0

freeSpace = float(input('How much free space in TB(Terabytes) do you have left? \n (Please only type a number...like maybe "6.6")  '))
print('\n \n \n')          #Just here to add space
freeSpace = freeSpace*1000 #This converts TB to GB
spaceUsed = round(5.6*45)  #This gets the amount of GB used per week 
                           #45videos/week at 5.6GB per video
spaceUsedDaily = spaceUsed/5    #This breaks the weekly amount down to daily, based on a 5day week
daysLeft = round(freeSpace/spaceUsedDaily, 2) #This gives the amount of days that the storage drive can continue taking in info
                                         #rounded to the nearest hundredths spot
print(f'You can continue downloading 9 videos a day(5.6GB ea) for {daysLeft} days before you run out of free space.')
#The 'f' before the string allows variables to be written inbetween {} to be written right into the sentence
print('\n \n \n ')








#B.)This program will determin how long it would take to upload a week's worth of data at 100Mb/s
import math
totalInMb = spaceUsed*1000*8 #Recalling spaceUsed "45vids x 5.6GB" and converted to MB


#The next is my conversion to seconds, minutes, hours. and writing them out
seconds = totalInMb/100
minutes = int(seconds/60)
hours = math.trunc(minutes/60)  #to cut off the decimal without rounding
minutes = (minutes%60)          #to cut of the whole number without rounding

print (f'''If you uploaded a week's worht of videos, it would take {hours} hours and {minutes} minutes.''')
print('\n \n \n')

