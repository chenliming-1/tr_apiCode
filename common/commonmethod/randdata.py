#!Date：2019/4/28 17:48
# !@Author：龚远琪
from module import *

subject = [1, 4, 5, 6, 7, 8, 9, 10, 12, 2082]       #科目
difflevel = [10021, 10015, 10001, 10016, 10023]     #难度
year = [10232, 10207, 10002, 10003, 10004, 10229, 10230, 10068, 10069, 10065, 10070, 10071, 10072, 10073, 10074, 10075]  #年份
region = [1, 9, 115, 124, 135, 152, 153, 154, 156, 161, 173, 207, 221, 1834]     #地区
picture = ['1-1.jpg', '3-1.png', '3-2.png', '3-3.png', '3-4.png', '3-5.png']    #图片
period = [10003, 100000282, 10001, 10002]     #学段
productline = ['DOUBLE_TEACHER', 'TEACHER_COLLEGE', 'HI_STUDY-INDIVIDUATION', 'HI_STUDY-FULLFILL_CLASS']  #产品线


class RandData(object):
    def getsubject(self):
        return random.choice(subject)

    def getdifflevel(self):
        return random.choice(difflevel)

    def getyear(self):
        return random.choice(year)

    def getregion(self):
        return random.choice(region)

    def getperiod(self):
        return random.choice(period)

    def getpicture(self):
        return random.choice(picture)

    def getproductline(self):
        return random.choice(productline)


randdata = RandData()