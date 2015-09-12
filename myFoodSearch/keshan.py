lis = []
myfile = open('list.txt','r')
data = myfile.readlines()
myfile.flush()
for item in data:
    i = 0
    while 1:
        if item[i] == ',':
            break
        i += 1
    lis.append(item[i+1:-1])
myfile.close()


def cal(list1,list2):
    tmp = []
    for i in range(1,279):
        if(i in list1 and i in list2):
            tmp.append(i)
    return tmp

def findID(foodname):
    tmplist = []
    file = open('dataList.txt','r')
    data = file.readlines()
    file.close()
    for line in data:
        if(foodname == (line.split(','))[0]):
            for i in line.split(',')[1:]:
                tmplist.append(int(i))
            return tmplist



############################################
#
# def foodToID(food):
#     mylist = []
#     IDlist = list(dic[food])
#     for i in range(len(IDlist)):
#         mylist.append(listtot[int(IDlist[i])])
#     return mylist

################################################################################
def searched(name):
    info = name
    lhydata = []
    infolist = info.split(" ")
    tmpinfo = findID(infolist[0])
    if(len(infolist)>1):
        for item in infolist:
            tmpinfo = cal(tmpinfo,findID(item))
    for num in tmpinfo:
        try:
            lhydata.append({'ID':num,'name':lis[num]})
        except:
            return 'no'
    print lhydata
    return 'yes'

print searched('egg')