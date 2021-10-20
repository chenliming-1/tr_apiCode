#!Date：2019/4/28 17:48
# !@Author：龚远琪
from module import *

subject = [1, 5, 6, 7, 8, 9, 10, 12, 17,2082]  # 科目
difflevel = [10021, 10015, 10001, 10016, 10023]  # 难度
year = [10232, 10207, 10002, 10003, 10004, 10229, 10230, 10068, 10069, 10065, 10070, 10071, 10072, 10073, 10074,
        10075]  # 年份
region = [1, 9, 115, 124, 135, 152, 153, 154, 156, 161, 173, 207, 221, 1834]  # 地区
picture = ['1-1.jpg', '3-1.png', '3-2.png', '3-3.png', '3-4.png', '3-5.png']  # 图片
period = [10003, 100000282, 10001, 10002]  # 学段
productline = ['DOUBLE_TEACHER', 'TEACHER_COLLEGE', 'HI_STUDY-INDIVIDUATION', 'HI_STUDY-FULLFILL_CLASS']  # 产品线
itemType = [1, 2, 3, 4, 5, 6, 7, 8, 101, 102, 103, 104, 105, 106, 107, 108, 109]  # 题型
itemMouldType = ['SINGLE_CHOICE', 'MULTIPLE_CHOICE', 'EXPLANATION', 'ENGLISH_WORD', 'WORD_CHOOSE', 'COMPREHENSIVE',
                 'ENGLISH_SENTENCE','CLOZE_TEST']  # 题型模版
paper_type = [10238, 10240, 10242, 10243, 10244, 10245, 10254, 10255, 10256, 10257, 10258, 10259, 10260, 10261]  # 套卷类型
school_year = [10247, 10248, 10249, 10250, 10251, 10252, 10253, 10254, 10256, 10257]   # 学年
paper_status = ['', 'DISABLED', 'OFF_SHELF', 'INIT']   # 试卷状态
course_type = [10025, 10026, 10027, 10028, 10029]   # 课程类型
lecture_source = ['USER_DEFINED', 'SYSTEM_IMPORT', 'USER_COPY', 'TEXT_BOOK_COPY', 'MY_DOCUMENT_COPY']  # 复制讲义来源


class RandData(object):
    def getsubject(self, length=1):
        return random.sample(subject, length)

    def getdifflevel(self):
        return random.choice(difflevel)

    def getyear(self):
        return random.choice(year)

    def getregion(self):
        return random.choice(region)

    def getperiod(self, length=1):
        return random.sample(period, length)

    def getpicture(self):
        return random.choice(picture)

    def getproductline(self):
        return random.choice(productline)

    def getitemtype(self):
        return random.choice(itemType)

    def getitemmouldtype(self):
        return random.choice(itemMouldType)

    def get_paper_type(self):
        return random.choice(paper_type)

    def get_school_year(self):
        return random.choice(school_year)

    def get_paper_status(self):
        return random.choice(paper_status)

    def get_course_type(self):
        return random.choice(course_type)

    def get_lecture_resource(self):
        return random.choice(lecture_source)


randdata = RandData()
# print(randdata.getRandArea())
