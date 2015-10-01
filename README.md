# nserver_py
Software Comprehensive Practice - News Server

[![Build Status](https://travis-ci.org/DlutCS/nserver_py.svg?branch=master)](https://travis-ci.org/DlutCS/nserver_py)

## 目录结构
```
nserver_py
    ./databases   数据库scheme文件
    ./models      model层
    ./tests       测试样例,文件以test_*.py方式命名
    ./utils       公共工具类
    ./views       view层
    ./templates   模板文件(submodule)
    ./assests     前端资源(submodule)
    app.py        入口文件
    app.yaml      主配置文件
    pip-req.txt   pip包依赖
```

## 安装
1.确保本地安装python2.7, pip, virtualenv, make工具可用

2.环境初始化, pip依赖安装
```
make sync
```
3.运行测试样例(可选)
```
make test
```
4.本地调试, 默认5000端口
```
make serve
```

## 建议工作流
0.fork origin仓库代码到个人仓库

1.设置remote/upstream链接到中央仓库, remote/origin链接到个人仓库

2.本地`master`分支跟踪upstream/master,只拉不推, 保持干净

3.在本地的`self-dev`分支上工作,`self-dev`分支跟踪`origin`/`self-dev`, 再次强调,不要在`master`和`prelease`上开发

4.开发之前进行rebase, 具体命令是:
```
git checkout prelease
git pull
git checkout 'self-dev' 
git rebase prelease
```

5.开发完成后推到`self-dev`, 提Pull Request到`origin`/`prelease`分支上,自行review合并跑预发环境的部署

6.发布时把`origin`/`prelease`提Pull Request到`origin`/`master`,同时打`tags`

## Pull Request规范
功能开发:
```
[Feature]xx功能

干了什么,描述下

```
Bug修复:
```
[Fix]修复了xxBug

怎么修复的
```

欢迎吐槽!

