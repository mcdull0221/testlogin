import unittest
from base.demo import RunMain
import json


class TestMerhod(unittest.TestCase):

    def setUpClass(cls):
        pass

    def setUp(self):
        self.run = RunMain()

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

    def tearDown(self):
        pass

    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
