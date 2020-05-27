# -*- encoding: utf-8 -*-
# @ModuleName: paper
# @Author：龚远琪
# @Date：2019/11/4 11:44
from common.commonmethod import randdata, cookie, todict
from histudy import request, log
import os


class Paper(object):
    def __init__(self):
        pass

    def create_paper(self):
        """
        创建一份试卷
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_addpaper.json'))
        data['request']['headers']['Cookie'] = cookie
        data['request']['json']['paperTextbookTypeId'] = randdata.get_paper_type()
        data['request']['json']['subjectId'] = randdata.getsubject()[0]
        data['request']['json']['yearId'] = randdata.getyear()
        data['request']['json']['schoolYearId'] = randdata.get_school_year()
        response = request.run_main(url=data['request']['url'], headers=data['request']['headers'],
                                    method=data['request']['method'], data=data['request']['json'])
        if response.status_code == 200:
            return response
        else:
            log.error('创建套卷失败！')

    def enable_paper(self, paper_id):
        """
        设置试卷为启用状态
        :param paper_id:
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_enable.json'))
        data['request']['headers']['Cookie'] = cookie
        data['name'] = data['name'].replace('201908169fb1aba57e1a407b8c9dea34eb33336b', str(paper_id))
        data['request']['url'] = data['request']['url'].replace('201908169fb1aba57e1a407b8c9dea34eb33336b',
                                                                str(paper_id))
        response = request.run_main(url=data['request']['url'], headers=data['request']['headers'],
                                    method=data['request']['method'], data=data['request']['json'])
        if response.status_code == 204:
            log.error('启用套卷成功！')
        else:
            log.error('启用套卷失败！')


paper = Paper()
# paper.create_paper()
