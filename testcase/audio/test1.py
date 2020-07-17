# -*- encoding: utf-8 -*-
# @ModuleName: test1.py
# @Author：龚远琪
# @Date：2020/7/17 14:04

from module import *


class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_a(self):
        """
        commonupload/通用上传：获取token接口成功的测试用例
        """
        a = 1
        print(a)

    @classmethod
    def tearDownClass(self):
        pass

