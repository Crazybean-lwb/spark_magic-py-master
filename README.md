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