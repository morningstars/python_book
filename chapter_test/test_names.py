from chapter_test import name_function

import unittest


# 创建测试类  继承自unittest.TestCase

class NamesTestCase(unittest.TestCase):

    # 会自动运行test开头的方法
    def test_name(self):
        formatted_name = name_function.get_formatted_name("janis", "joplin")
        print(formatted_name)
        self.assertEqual(formatted_name, "Janis Joplin")


if __name__ == '__main__':
    unittest.main()
