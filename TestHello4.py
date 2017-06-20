#针对测试类的 setUp 和 tearDown
class TestHello4:
	def setUp():
		print('set UP')
	def tearDown(self):
		print('tear down')
	def TestCase1(self):
		print('test case1')
		assert 1==1
	def TestCase2(self):
		print('test case2')
		assert False
#-v  看nosetests的执行信息。比如当前正在执行哪个测试。
# -s  不拦截标准输出，使用了这个参数才能看到print 的信息。
# -h  帮助，这个最重要，哈哈

#看看所在的位置就好了。nose 会针对每个类内部的测试用例创建单独的类实例，所以执行顺序如下：
#setUp –> TestCase1 –> tearDown –> setUp –> TestCase2 –> tearDown
#针对package的 setUp 和 tearDown
#把setUp() 和 tearDown() 写在package __init__.py 中就好了，整个package 就只执行一次这个 setUp 和 tearDown
