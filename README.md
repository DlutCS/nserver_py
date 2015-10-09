# nserver_py
Software Comprehensive Practice - News Server

- 线上版本(`master`):
[![Build Status](https://travis-ci.org/DlutCS/nserver_py.svg?branch=master)](https://travis-ci.org/DlutCS/nserver_py)
- 预发布版本(`prelease`):
[![Build Status](https://travis-ci.org/DlutCS/nserver_py.svg?branch=prelease)](https://travis-ci.org/DlutCS/nserver_py)

## 目录结构
```
nserver_py
    ./databases   数据库scheme文件
    ./models      model层
    ./tests       测试样例,文件以test_*.py方式命名
    ./utils       公共工具类
    ./views       view层
        ./api     移动应用api接口
    ./templates   模板文件(submodule)
    ./assests     前端资源(submodule)
    app.py        入口文件
    default.cfg   主配置文件
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
1.checkout 主仓库代码到本地

2.在主仓库上新建个人分支`dev-self`

3.在本地的`dev-self`分支上工作,`dev-self`分支跟踪`origin`/`dev-self`, 再次强调,不要在`master`和`prelease`上开发或推送

4.开发之前进行rebase, 具体命令是:
```
git checkout prelease
git pull
git checkout 'dev-self' 
git rebase prelease
```

5.开发完成后推到`dev-self`, 提 Pull Request到`origin`/`prelease`分支上,邀请@他人或自行Review

6.Review完毕并确认CI通过后, 合并Pull Request,等待CI的prelease部署

7.正式上线时把`origin`/`prelease`提Pull Request到`origin`/`master`,同时打`tag`

## 前端模板工作流
0. 前端仓库 `DlutCS/nclient_asset`

1. 同样含有`master`和`prelease`对应的分支

2. 正常开发时, 可以对模板做数据输出测试，但不能提交对HTML有影响的修改

3. 前端模板 & 资源发布流程

3.1 在`nclient_asset`部署完成`prelease`或`master`到服务器

3.2 获取部署的`commit-id`, 修改`nserver_py`对应环境配置文件中的资源Hash

3.3 正常推送开发


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

