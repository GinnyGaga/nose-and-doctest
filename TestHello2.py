def setUp():
	print('setUp here')
def tearDown():
	print('tearDown here')
def TestF1():
	a=3
	b=3
	print('test F1')
	assert a==b
def TestF2():
	print('test F2')
	assert True
#针对模块的 setUp 和 tearDown
#注意：不是针对类的，是一个模块，python的一个模块也可以理解为一个文件
#nosetests -s 执行顺序为 setUp() –> TestF1() –> TestF2() –> tearDown()
