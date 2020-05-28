# -*- encoding: utf-8 -*-
# @ModuleName: tempaper.py
# @Author：龚远琪
# @Date：2020/5/28 11:12
from common.commonmethod import todict, randdata,cookie
from histudy import request, log
import time, os


class TemPaper(object):
    def add_tempaper(self):
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'tempaper_addtempaper.json'))
        data['request']['headers']['Cookie'] = cookie
        get_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        paper_name = get_time.replace('/', '') + '临时试卷'
        data['request']['json']['name'] = paper_name
        data['request']['json']['periodId'] = randdata.getperiod()[0]
        data['request']['json']['subjectId'] = randdata.getsubject()[0]
        res = request.run_main(url=data['request']['url'], headers=data['request']['headers'],
                               method=data['request']['method'], data=data['request']['json'])
        if res.status_code == 200:
            return res
        else:
            log.error('创建临时试卷失败！')


tempaper = TemPaper()
