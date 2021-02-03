### 在当前环境中安装spark magic

第一步：从gitlab下载

地址: https://github.com/liuweibin6566396837/spark_magic-py-master

第二步: 切换到需要安装工具包的环境

例如:

```
source /opt/app/anaconda3/bin/activate
```

第三步: setup安装工具包

切换到spark_magic-py-master/根目录下
执行：

```
python setup.py build
python setup.py install
```

第四步: 拷贝模块到当前环境的site-package下

一般来说，第四步是不需要的，但是site-package下没有自动生成spark_magic模块工具包(哪位大佬知晓，可以告知一下)

```
cp -r spark_magic xxx/site-packages
```

使用pip list可以看到spark-magic模块
安装成功！！！

注意：在console中直接引包会出现`NameError: name 'get_ipython' is not defined`错误无需理会，这是由于当前没有ipython进程获取不到该进程，而在jupyter起服务时会起该进程

### 在notebook中如何调用spark magic

第一步：引入spark magic 第三方工具包

```python
from spark_magic.sparkmagic import *
```

第二步：调用spark line magic(默认配置) 或者 cell magic(自定义配置)


```python
%pyspark           # line magic
```

```python
%%pyspark          # cell magic
spark.app.name:jupyter-user
spark.pyspark.driver.python:/opt/app/anaconda3/bin/python
spark.pyspark.python:/opt/app/anaconda3/bin/python
spark.driver.memory:2g
spark.executor.memory:2g
spark.executor.cores:3
spark.executor.instances:1
```

第三步：引用会话

```python
spark, sc = _
```

