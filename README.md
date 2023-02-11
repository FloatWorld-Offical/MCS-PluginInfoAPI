# MCS-PluginInfoAPI
![Status](https://img.shields.io/badge/Build-Success-brightgreen)
![Status](https://img.shields.io/badge/Status-ContinuousUpdate-brightgreen)
![Status](https://img.shields.io/badge/Version-v0.1-blue)
![Status](https://img.shields.io/badge/Team-FloatWorld-blue)
![Status](https://img.shields.io/badge/Author-皇橙籽-blue)
![Status](https://img.shields.io/badge/Language-Python-blue)
### 本程序版本号仅会在整体更新时进行更新，单个模块更新不影响
### 软件运行环境
- Python 3.11.2
- Django 4.1.6（可以使用pip下载）
- mysql-connector-python
- json（标准库）

### 适配数据库类型
- MySQL
- SQLite(计划中)
- MongoDB(计划中)

### 适配Minecraft插件列表
- PlayerPoints

### 地址结构说明
本API的默认访问地址结构如下
http(s)://地址/api/插件名/查询模块/查询参数

### API文档
暂未编写

### 使用教程
[必要部分]  
1. 完成上述运行环境的安装
2. 在Release中下载程序基础包(MCS-PluginInfoAPI_Base.zip)
3. 解压至任意文件夹
4. 在MCS_PluginInfoAPI文件夹中取消您想要打开的模块的注释
5. 从Release中下载对应插件的读取模块
6. 修改data文件夹中对应插件的数据
7. 修改启动参数(公网IP需至MCS_PluginInfoAPI/settings.py中添加允许的IP)

[非必要部分]
- 下载机器人管理程序(用于快捷调整机器人设置，您也可以选择直接前往配置文件进行调整)

### 支持作者
您可以通过添加作者的QQ群来支持作者的开发工作  
您也可以选择向作者打钱(赞助或定制)来直接支持作者的工作

### 联系作者
您可以通过联系作者来第一时间获得更新消息/进行赞助/进行深度定制  
QQ: 2232195659  
QQBot: 431157671（用于测试、自动处理简单事务）  
Email(Team): offical@floatworld.work  
Email(Author): orange_hcz@floatworld.work
