import unittest

"""单元测试 断言方法
"""

__author__ = ""
__copyright__ = "Copyright 2016-2017, hython.com"


person = {'name': 'Mike', 'age': 45}
numbers = [1, 3, 4, 33, 5, 65]
s = '测试 hython.com'


class TestAssert(unittest.TestCase):
    def test_assert_method(self):
        self.assertEqual('Mike', person.get('name'))
        self.assertIn('hython', s)
        # self.assertIsNone('Name', None)


if __name__ == '__main__':
    unittest.main()
