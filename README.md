说明：

1. 目前暂时只支持Ubuntu系统的服务器的自动配置。个人电脑的配置支持Ubuntu和Fedora。
2. 选择开发环境还是集群环境：服务器一般没有外设，在服务器上直接开发一般是很不方便的事情。在开发spark应用的时候，我们一般先在个人电脑上开发和测试应用，然后再到服务器上运行。如果你希望开发spark应用，那么选择配置开发环境。如果你这是一台服务器，要在上面运行spark应用，并进行集群运算，那么配置集群环境。
3. 如果你从没有配置过spark环境，那么我也建议你先从配置开发环境开始，在你自己的电脑上配置spark。集群环境比开发环境更复杂。

# 从github上下载和解压build工具

如果不喜欢命令行的话，你可以直接在github图形界面上Download。图形界面应该也可以直接解压。

# 配置spark开发环境

## 下载和解压spark安装包

因为spark安装包太大了放不进来，所以需要你自己下载。

从spark官网上下载预编译hadoop的spark压缩包，并解压。

```sh
tar -xvzf ~/Download/spark-2.2.0-bin-hadoop2.7.tar.gz
```

## 安装

spark的开发环境不需要运行脚本`build.py`。

有两种方法可以使用脚本安装spark。

### 移动压缩包到指定地点

你可以将解压完的spark文件目录移动到`somepath/build/src/spark/`目录下(把`somepath`换成这个README文件的父目录)。

例如，我下载的spark压缩包名叫`spark-2.2.0-bin-hadoop2.7.tar.gz`，下载到了`~/Download`目录下。解压它，解压后文件名是`spark-2.2.0-bin-hadoop2.7`，把它移动到`somepath/build/src/spark/`目录下：

```sh
# 假如我的build文件夹在~/build
mv ~/Download/spark-2.2.0-bin-hadoop2.7 ~/build/src/spark
cd ~/build/src/
# 如果你的发行版是fedora，就--ubuntu换成--fedora，注意全部是小写
python spark.py --ubuntu
```

### 或者，在运行脚本的时候指定目录

```sh
python spark.py -f ~/Download/spark-2.2.0-bin-hadoop2.7 --ubuntu
```

# 配置服务器的spark运行环境

## 下载和解压

和配置开发环境时一样，你需要先下载和解压spark安装包。

## 安装

集群模式的安装需要使用脚本`build.py`，并需要root权限。

同样的，你可以选择将spark目录移动到`somepath/build/src/spark/`，或者在运行脚本时指定`-f`参数。

```sh
sudo python build.py --ubuntu
# 或者
sudo python build.py -f ~/Download/spark-2.2.0-bin-hadoop2.7 --ubuntu
```

# 模块解析

## Basis

Basis模块更新软件源和软件包，并安装基础应用git。

## Python

Python模块安装pip，更新pip，并安装常用模块包。

## Spark

Spark模块安装java，并将spark环境变量写入配置文件。

1. 将用户下载的spark文件移动到目标目录下。目标目录会根据命令行参数而改变。
2. 配置spark路径和python路径，目标profile会根据命令行参数而改变。
3. 更改spark日志级别从INFO到WARN。

## Conf_spark

这个模块负责spark集群的配置。

1. 写入`hosts`文件
2. 写入`slaves`文件
3. 写入`spark-env.sh`文件
