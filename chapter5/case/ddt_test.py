#coding=utf-8
import unittest
import ddt
@ddt.ddt
class DdtTest(unittest.TestCase):
    data = ((3,4),(4,6),(-3,1))
    print(data)   #一个元祖 ((3, 4), (4, 6), (-3, 1))
    print(*data)    #三个元组(3, 4) (4, 6) (-3, 1)
    @ddt.data(*data)   #这里加*后会将返回数据分为一个个的元组
    @ddt.unpack       #unpack分解list或者tuple
    def testMethod(self,a,b):
        print(a + b)

if(__name__ == "__main__"):
    unittest.main()