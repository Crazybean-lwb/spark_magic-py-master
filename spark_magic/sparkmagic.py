# -*- encoding: utf-8 -*-
# This code can be put in any Python module, it does not require IPython
# itself to be running already.  It only creates the magics subclass but
# doesn't instantiate it yet.
# The class MUST call this class decorator at creation time

import findspark
findspark.init("/usr/hdp/2.6.2.0-205/spark2/")  # 这个args要指明SPARK_HOME 例如:findspark.init("/usr/hdp/2.6.2.0-205/spark2/")
from pyspark.sql import SparkSession
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)


@magics_class
class SparkMagics(Magics):

    @line_magic
    def lmagic(self, line):
        "my line magic"
        print("Full access to the main IPython object:", self.shell)
        print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
        return line

    @cell_magic
    def cmagic(self, line, cell):
        "my cell magic"
        return line, cell

    @line_cell_magic
    def pyspark(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            spark = SparkSession.builder.appName("jupyter-shell") \
                .config("spark.master", "yarn") \
                .config("spark.submit.deployMode", "client") \
                .config("spark.pyspark.python", "/opt/app/anaconda3/bin/python") \
                .config("spark.pyspark.driver.python", "/opt/app/anaconda3/bin/python") \
                .config("spark.driver.memory", "1g") \
                .config("spark.executor.memory", "1g") \
                .config("spark.executor.cores", "2") \
                .config("spark.executor.instances", "4") \
                .getOrCreate()
            sc = spark.sparkContext
            return spark, sc
        else:
            print("Called as cell magic")
            properties = {}
            args = cell.split()
            for arg in args:
                properties[arg.split(":")[0]] = arg.split(":")[1]

            # 判断一些基本配置是否存在, 设置默认配置
            if "spark.app.name" not in properties.keys():
                properties["spark.app.name"] = "jupyter-shell"
            if "spark.pyspark.driver.python" not in properties.keys():
                properties["spark.pyspark.driver.python"] = "/opt/app/anaconda3/bin/python"
            if "spark.pyspark.python" not in properties.keys():
                properties["spark.pyspark.python"] = "/opt/app/anaconda3/bin/python"
            if "spark.driver.memory" not in properties.keys():
                properties["spark.driver.memory"] = "2g"
            if "spark.executor.memory" not in properties.keys():
                properties["spark.executor.memory"] = "2g"
            if "spark.executor.cores" not in properties.keys():
                properties["spark.executor.cores"] = "1"
            if "spark.executor.instances" not in properties.keys():
                properties["spark.executor.instances"] = "2"

            spark = SparkSession \
                .builder \
                .config("spark.app.name", properties["spark.app.name"]) \
                .config("spark.master", "yarn") \
                .config("spark.submit.deployMode", "client") \
                .config("spark.pyspark.driver.python", properties["spark.pyspark.driver.python"]) \
                .config("spark.pyspark.python", properties["spark.pyspark.python"]) \
                .config("spark.driver.memory", properties["spark.driver.memory"]) \
                .config("spark.executor.memory", properties["spark.executor.memory"]) \
                .config("spark.executor.cores", properties["spark.executor.cores"]) \
                .config("spark.executor.instances", properties["spark.executor.instances"]) \
                .getOrCreate()
            sc = spark.sparkContext
            return spark, sc


# In order to actually use these magics, you must register them with a
# running IPython.

def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    # You can register the class itself without instantiating it.  IPython will
    # call the default constructor on it.
    ipython.register_magics(SparkMagics)

ipy = get_ipython()
ipy.register_magics(SparkMagics)