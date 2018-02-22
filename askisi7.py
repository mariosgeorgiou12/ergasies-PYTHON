import datetime
day = datetime.date.today()
weekday = day.isoweekday()
day_str= day.strftime("%d-%m-%Y")
counter=0

print "Simerini imerominia:",day_str
print ""
def increase(day, years):
    try:
        return day.replace(year = day.year + years)
    except ValueError:
        return day + (date(day.year + years, 1, 1) - date(day.year, 1, 1))

for i in range (1,11):
    nextyear = increase(day,i)
    dayofweek = nextyear.isoweekday()
    if dayofweek == weekday:
        counter+=1
        if counter==1:
            print "Idies meres sta epomena 10 xronia"
        nextyear= nextyear.strftime("%d-%m-%Y")
        print nextyear

print ""
print "Synolika:",counter
