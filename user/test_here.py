import datetime
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


datetimeFormat = '%Y/%m/%d %H:%M:%S'
time1 = '2016/06/16 10:01:28'
time2 = '2016/05/16 11:31:28'
time_left = datetime.datetime.strptime(time1, datetimeFormat) - datetime.datetime.strptime(time2,datetimeFormat)

print((str(time_left)))
print (int(str(time_left)[-4]) or int(str(time_left)[-7]))

print(int(str(time_left).split(',')[0].split(' ')[0]))

if ',' in str(time_left):
    int(str(time_left)[0])
else:
    int(str(time_left)[-4]) or int(str(time_left)[-7])

a=[]
a.append(('arslan','studend'))

print(a)
if ('arslan','studend') in a:
    print('okay')

#a.append(('arslan','job'))
if ('arslan','job') in a:
    print('a')