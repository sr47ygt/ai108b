import random as r

role =[]
n = ['阿貓','阿狗','我','小明']
f = ['炒販','便當','泡麵','炸雞','拉麵','水餃','三明治','漢堡']
d = ['多多綠','奶茶','紅茶','烏龍茶','清茶','柳橙汁','豆漿']
t = ['中午','晚上','宵夜','早餐']
da = ['今天','明天','後天']



def S():
    return  N() + DAY() + TIME() + '想吃' + Food() + '配' + DRINK()

def N():
    return r.choice(n)

def Food():
    return r.choice(f)

def DRINK():
    return r.choice(d)

def TIME():
    return r.choice(t)

def DAY():
    return r.choice(da)

print(S())