import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
from module import random
import os


class TestReviewAnswer(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_review_answer.json'))
        self.data['request']['headers']['Cookie'] = cookie
        like_or_not = random.choice(["true", "false"])
        self.data['name'] = self.data['name'].replace('false', like_or_not)
        self.data['request']['url'] = self.data['request']['url'].replace('false', like_or_not)

    def test_review_answer(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_review_answer: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('item/test_review_answer: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
