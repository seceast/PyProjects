

## 一、Appium 环境安装



![1558276288864](D:\data\雨泽\typora图片\1558276288864.png)



### 1、APP 测试和 Web 测试的区别

![1558276365325](D:\data\雨泽\typora图片\1558276365325.png)



![1558276381905](D:\data\雨泽\typora图片\1558276381905.png)



- appium 独立软件； ==> webdriver
- appium-python client  ==> selenium-python
- adb ==> js ==> apt-abundlec
- 安卓 sdk ==》 浏览器环境
- java jdk ==> 



### 1、安装环境打包地址：

链接：https://pan.baidu.com/s/1L_XG8880_FtBPc54sddbNA 
提取码：eizo 
复制这段内容后打开百度网盘手机App，操作更方便哦



### 2、Appium环境安装说明



####  **1、安装Microsoft .NET Framework 4.5**

检测本机已安装的程序中，是否已经安装Microsoft .NET Framework 4.5及以上的版本。

如果没有安装，则双击运行如下文件：net4.5.1.exe

####  **2****、安装node-v6.11.4-x64.msi**

   双击运行，安装appium的依赖环境，node.js.  8+

####  **3、安装appium**

   双击运行 appium-desktop-Setup-1.2.4.exe。系统

   也可以去官方网站下载最新的appium版本。新版appium提供了元素定位的功能。

官方网站地址：<http://appium.io/>


appium 的安装位置。 1、 给所有的用户安装。2、给当前用户安装。非常长。（推荐）


####  **4、安装JDK**

   安装JDK1.8及以上版本。`尽量装高版本，64位版对应。`

####  **5、安卓ADT工具** 提供安卓的sdk 和工具。 新手继承包

http://tools.android-studio.org/index.php/adt-bundle-plugin

- 双击解压 adt-bundle-windows-x86_64-20140702.zip, studio

- 配置环境变量：

添加ANDROID_HOME环境变量，配置sdk根目录。

在以上的截图中，

ANDROID_HOME=D:\software\adt-bundle-windows-x86_64-20140702\sdk

- 在PATH变量中添加adb所有的目录：

;%ANDROID_HOME%\platform-tools

- 检测：

进入cmd命令行，输入adb version

能够正常显示adb的版本就okay.

#### 6、夜神模拟器或这真机

#### 7、**安装appium python客户端**

使用python的pip命令，直接在线安装：

```bash
pip install Appium-Python-Client
```



#### 8、检测安装成功

1. Appium。直接打开访问是否成功。
2. adb
3. 模拟器



### 3、跟新 adt 里面的 sdk_manager.exe

对于比较新的版本，老的 adb 和 android_platform 会报错。所以需要更新对应的 api 和 adb. 点击 sdk_manager, 更新最新的 sdk， 安卓的 api 是向下兼容的，只需要下载最新版的，低版本的也能用。

![1564553653156](D:\data\雨泽\typora图片\1564553653156.png)



如果不能立即刷新，需要点击 tools -> option, 添加镜像：

![1564553752008](D:\data\雨泽\typora图片\1564553752008.png)



可以用的镜像地址：

1、中科院开源协会镜像站地址:

IPV4/IPV6 : http://mirrors.opencas.ac.cn 端口：80

2、北京化工大学镜像服务器地址：

IPv4: http://ubuntu.buct.edu.cn/  端口：80

IPv4: http://ubuntu.buct.cn/  端口：80

IPv6: http://ubuntu.buct6.edu.cn/  端口：80

3、大连东软信息学院镜像服务器地址:

http://mirrors.neusoft.edu.cn  端口：80



### 4、**安装夜神模拟器**

参看夜神模拟器安装文件夹，里面有安装步骤和说明。

记得把 带有环境变量的 adb 命令命名到 夜神模拟器的 adb_nox



#### 更新夜神手机系统版本

夜神多开形式进行修改：

![1564553917165](D:\data\雨泽\typora图片\1564553917165.png)









## 二、APP 测试概述



### 2、Appium 是什么？

安卓，自己的自动化测试框架：uiautomator

苹果：xcui,  python



![1564558845920](D:\data\雨泽\typora图片\1564558845920.png)

Appium 旨在满足移动端自动化需求的理念，概述为以下四个原则：


- 你没有必要为了自动化而重新编译你的应用或者以任何方式修改它。
      Android/IOS系统自带框架
- 你不应该被限制在特定的语言或框架上来编写运行测试。
      WebDriver API
       客户端-服务器协议（称为 JSON Wire Protocol）
-  移动端自动化框架在自动化接口方面不应该重造轮子。
      WebDriver  - Web 浏览器自动化的标准
       附加可用于移动端自动化的 API 方法
- 移动端自动化框架应该开源，不但在名义上而且在精神和实践上都要实至名归。
      Appium开源
- 可以做混合应用，可以同时做原生应用和 H5, app嵌套 html
- html --> 嵌套，iframe  webview



### 3、Appium 自动化测试的流程图



### 4、系统官方的自动化框架

iOS 9.3 及以上：苹果的 XCUITest
iOS 9.3 及以下：苹果的 UIAutomation  object-c swift
Android 4.2+: 谷歌的 UiAutomator
Android 2.3+: 谷歌的 Instrumentation（通过绑定另外的项目—— Selendroid 提供 Instrumentation 的支持） kotlin





