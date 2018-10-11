import unittest
from base.demo import RunMain
import json
import HTMLTestRunner
import os


class PortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.run = RunMain()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            # 'errorCode': 1007
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        self.assertIn('"errorCode":1007', res)
        globals()['userid'] = 1000909

    def test_02(self):
        print(globals())
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        self.assertIn('"errorCode":1007', res)
        # if res.__contains__('"errorCode":1001'):
        #     print('测试通过')
        # else:
        #     print('测试失败')


if __name__ == '__main__':
    # filepath = "../report/htmlreport.html"
    # fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(PortTest('test_01'))
    suite.addTest(PortTest('test_02'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test')
    # runner.run(suite)
