# -*- encoding: utf-8 -*-
# @ModuleName: lecture.py
# @Author：龚远琪
# @Date：2020/5/28 11:36
from histudy import log, request, randMethod
from common.commonmethod import cookie, todict, randdata
from module import jsonpath, random
import os


class Lecture(object):
    def add_folders(self):
        """
        新建文件夹
        :return:
        """
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_addfolders.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['name'] = 'AT_' + randMethod.getMessage(5)
        res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               method=self.data['request']['method'], data=self.data['request']['json'])
        if res.status_code == 201:
            return res
        else:
            log.error('创建文件夹失败！')

    def add_lecture(self):
        """
        新建文档
        :return:
        """
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_addlecture.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['name'] = 'AT_' + randMethod.getMessage(5)
        self.data['request']['json']['parentId'] = 2322
        self.data['request']['json']['productCode'] = randdata.getproductline()
        res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               method=self.data['request']['method'], data=self.data['request']['json'])
        if res.status_code == 201:
            return res
        else:
            log.error('创建文件夹失败！')

    def delete_files(self, ids):
        """
        批量删除文件夹
        :return:
        """
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_deletefiles.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data["request"]['json']['ids'] = ids
        res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               method=self.data['request']['method'], data=self.data['request']['json'])
        if res.status_code == 204:
            return res
        else:
            log.error('删除文件夹失败！')

    def get_folders_tree(self, subjectId=8, periodId=10001):
        """
        获取文件树
        :return:
        """
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_getfolderstree.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['params']['periodId'] = periodId
        self.data['request']['params']['subjectId'] = subjectId
        res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               method=self.data['request']['method'], data=self.data['request']['json'])
        if res.status_code == 200:
            return res
        else:
            log.error('获取文件夹树失败！')

    def get_rand_folder(self):
        """
        获取随机文件夹
        :param point_tree:
        :return:
        """
        try:
            get_folders_tree_res = self.get_folders_tree()
            folders_tree = get_folders_tree_res.json()
            folders_id_list = jsonpath(folders_tree, "$..id")
            folders_id = random.choice(folders_id_list)
            return folders_id
        except AssertionError as error:
            log.error("获取随机文件夹失败，失败原因："f'{error}')


lecture = Lecture()
