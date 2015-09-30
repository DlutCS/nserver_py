# nserver_py
Software Comprehensive Practice - News Server


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
0.fork中央仓库代码到个人仓库

1.设置remote/upstream链接到中央仓库, remote/origin链接到个人仓库

2.本地master分支跟踪upstream/master,只拉不推, 保持干净

3.在本地的dev分支上工作,dev分支跟踪origin/dev, 再次强调,不要在master上开发

4.开发之前进行rebase, 具体命令是:
```
git checkout master
git pull
git checkout dev 
git rebase master
```

5.开发完成后推到origin/dev, 提Pull Request到中央仓库的master分支上,等待review合并

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

