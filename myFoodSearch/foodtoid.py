#-*-coding:utf-8-*-
# list = []
# myfile = open('templates/list.txt','r')
# file = open('templates/idToFood.py','w')
# data = myfile.readlines()
# for i in range(len(data)):
#     dic = {}
#     tmplist = data[i].split(',')
#     dic['ID'] = tmplist[0]
#     tmp = tmplist[1].replace('\n','')
#     dic['name'] = tmp
#     list.append(dic)
# print>>file, list

# def findListDic():
#     lhydic = {}
#     myfile = open('templates/list.txt','r')
#     data = myfile.readlines()
#     for i in range(len(data)):
#         info = data[i].split(',')
#         lhydic[info[1].replace('\n','')] = (int(info[0]),)
#     return lhydic
# keshan = open('keshan.txt','w')
# print>>keshan, findListDic()
def idToFood():
    lhylist=[]
    myfile = open('templates/list.txt','r')
    data = myfile.readlines()
    for i in range(len(data)):
        dic = {}
        info = data[i].split(',')
        dic['ID'] = info[0]
        tmp = info[1].replace('\n','')
        dic['name'] = tmp
        lhylist.append(dic)
    return lhylist
lhydic = {}
def findListDic():

    myfile = open('templates/list.txt','r')
    data = myfile.readlines()
    for i in range(len(data)):
        info = data[i].split(',')
        lhydic[info[1].replace('\n','')] = (int(info[0]),)
    return lhydic

def foodToID(food):
    listtot = idToFood()
    mylist = []
    lhydic = findListDic()
    IDlist = list(lhydic[food])
    for i in range(len(IDlist)):
        mylist.append(listtot[int(IDlist[i])])
    return mylist

################################################################################
def searched(food):
    list1 = foodToID(food)
    return list1
print searched('Genoise')
print lhydic
