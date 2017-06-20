#针对每个函数设置setUp 和 tearDown
def Func1_setup():#函数名随意，不是以Test打头就行，否则会被当作case
	print('case 1 setup')
def Func1_teardown():
	print('case 1 teardown')
def Test_func1():
	print('Test 1')

	assert True
def Func2_setup():
	print('case 2 setup')
def Func2_teardown():
	print('case 2 teardown')
def Test_func2():
	print('Test 2')
	assert True

Test_func1.setUp = Func1_setup
Test_func1.tearDown = Func1_teardown

Test_func2.setUp = Func2_setup
Test_func2.tearDown = Func2_teardown

#重点是最后的四行，分别指定了Test_func1 和 Test_func2 的setUp 和 tearDown 分别是谁。
#执行顺序：Func1_setUp –> Test_func1 –> Func1_teardown –> Func2_setup –> Test_func2 –> Func2_teardown
#nose还提供了另外一种叫做with_setup的方法，以Test_func1为例：
#@with_setup( Func1_setup, Func1_teardown )
#def Test_func1( ):
#      …
#这样就不需要后边那几行去指定了。也挺好用，不过要记得引入with_setup：from nose.tools import with_setup
