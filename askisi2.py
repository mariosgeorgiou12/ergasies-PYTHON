import urllib2
import datetime
import json

day=datetime.datetime.now()
save_days=[]
save_wins=[]

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s

print "Doste 10 arithmous (1-80)"
nums = raw_input()
nums = map(int, nums.split())

for i in range(31):
    day= day - datetime.timedelta(days=1)
    date_str= day.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']

    sum_wins_day=0
    for k in klhrwseis:
        tmp=k["results"]
        epitixies=compare_lists(nums,tmp)
        if (epitixies>4):
            sum_wins_day+=1
    save_wins.insert(i,sum_wins_day)
    save_days.insert(i,date_str)

max_wins=save_wins[1]
max_day=save_days[1]
for i in range(31):
    if (max_wins < save_wins[i]):
        max_wins=save_wins[i]
        max_day=save_days[i]

print "Stis", max_day, "tha eixate ta perissotera kerdi me", max_wins, "epitixies"
