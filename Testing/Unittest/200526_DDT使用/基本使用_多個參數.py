import unittest
import ddt


# 測試用例類(必須繼承Unuttest TestCase類)
@ddt.ddt  # 要在用例中使用ddt，需要先在測試類上導入ddt(@ddt.ddt)
class MyTestCase(unittest.TestCase):

    @ddt.data((1, 2), (3, 4))
    @ddt.unpack  # 當用例參數不只一個時須使用，unpack用於拆包
    def test_a(self, x, y):
        print(x+y)


if __name__ == '__main__':
    unittest.main()
