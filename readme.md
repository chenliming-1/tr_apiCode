1. git clone  http://gitlab.xstudy.com.cn/test/tr_api.git

2. 执行init.py命令进行安装包

3. 执Main.py进行执行测试用例

4. 打开Report目录下的report.html文件查看报告

5. 新增第三方包中应注意：
	* requiremenst中需要加入你要引入的第三方包
	* 在module的init.py文件中导入该第三方包后续都可以直接使用:
```python
import unittest
__all__ = ['unittest']
```

