from operator import itemgetter

global numFlowers
#input by users
numFlowers=int(input())
temp=[]
for i in range(numFlowers):
    temp.append(input().split())


bDate=[]
fDate=[]
bfDate=[]
#string to int and date to numbet to make the comparing easy
for i in range(numFlowers):
    #if the user input empty, this line will remove it in the list
    if not temp[i]:
        i
    else:
        if int(temp[i][1])<10:
            bDate.append(int(temp[i][0]+'0'+temp[i][1]))
        else:
            bDate.append(int(temp[i][0]+temp[i][1]))
        if int(temp[i][3])<10:
            fDate.append(int(temp[i][2]+'0'+temp[i][3]))
        else:
            fDate.append(int(temp[i][2]+temp[i][3]))
#this line will recalculate the length of the list from inputing empty
numFlowers=len(bDate)
#move all the blossom date and end date into one list
for i in range(numFlowers):
    bfDate.append([bDate[i], fDate[i]])
#this line will sort the multilist([][]) by the blossom date(first section)
bfDate.sort(key=itemgetter(0))
sdate=301
edate=301
count=0
location=0
print(bfDate)
for i in range(numFlowers):
    if bfDate[i][0] <= 301 and bfDate[i][1] > edate:
        sdate=bfDate[i][0]
        edate=bfDate[i][1]
        count=1
        location = i + 1

print(sdate, edate, location, count)
#function to calculate the minimum number of the flowers
def search(c, l, e):
    sdate1=0
    edate1=0
    if e < 1201 and l < numFlowers:
        for i in range(l, numFlowers):
            if (bfDate[i][0] <= e) and bfDate[i][1]>edate1:
                sdate1 = bfDate[i][0]
                edate1 = bfDate[i][1]
                temp1=i
        e=edate1
        print(sdate1,e)
        c = c + 1
        l = temp1 + 1
        return search(c, l, e)
    else:
        return c, e

print(numFlowers)
count, edate = search(count, location, edate)
if edate < 1201:
    print(0)
else:
    print(count)
