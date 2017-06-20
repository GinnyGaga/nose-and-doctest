def TestHello():
	a=3
	b=3
	assert a==b
#这是最简单的使用nose执行测试case的结果

#nosetests 命令就是执行case的。它会自动查找当前目录下包含“Test”字样的目录和文件（文件里的python函数也已Test开头），然后执行，返回case执行成功与否。
