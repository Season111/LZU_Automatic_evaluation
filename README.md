# 兰州大学自动评教
代码参考自LZU的hollowman6,他账号被封以后就找不到类似的脚本了。

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/LZU-Auto-Course-Evaluation-Feedback)](../../graphs/commit-activity)

[![Followers](https://img.shields.io/github/followers/Season111?style=social)](https://github.com/Season111?tab=followers)
[![watchers](https://img.shields.io/github/watchers/Season111/LZU_Automatic_evaluation?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/Season111/LZU_Automatic_evaluation?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/Season111/LZU_Automatic_evaluation?style=social)](../../network/members)

(English version is down below)

**可直接运行脚本中的.exe文件，之后登陆账号，即可完成评教，值得注意的是，由于调用的是chromedriver，必须使用谷歌浏览器才可以正常使用。**
**使用python脚本的话可以自行下载自己浏览器对应的driver，[Chrome Driver](https://chromedriver.chromium.org),[Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)**

已知bug：
在进行医学校区评教时，会出现无限弹出医学校区评教而无法正常进行期末评教的情况

[Python库依赖](../../network/dependencies)

**使用edge浏览器**
此程序使用Python的selenium库，使用如果使用edge浏览器的话，需要在程序执行目录下放置了[Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)，并且要注意浏览器的版本号要和Edge Driver保持一致。具体可自行搜索selenium的具体使用教程。

此程序适用于 `http://qa.lzu.edu.cn:8081` 页面的评教。


## 使用方法

只要在程序运行开始的页面输入你的账号和密码，并点击登录，程序将会自动为你评教。

![](login.png)

程序会自动为每个老师给予最高的评价，并在需要填写文字处填写上“好”。

如果该课程老师数量大于3个，程序会首先进行课程的评教，再进行老师的评教。

**注：**：如果遇到有的老师被跳过的问题，可能是由网络状况引起的，建议再次运行一下。

## 链接

* [兰州大学自动评教 脚本](LZU-Auto-Course-Evaluation-Feedback.py)

测试于2021年12月29日，2021-2022学年第一学期期末评教，2021年11月12日, 2021-2022学年第一学期期中评教。


**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***

# LZU Auto Course Evaluation Feedback

[Python library dependency](../../network/dependencies)

Using selenium to realize the function. Before using, make sure that Google Chrome browser is installed on the computer, and [Chrome Driver](https://chromedriver.chromium.org) is placed in the programme execution directory.

The programme is suitable for course evaluation at `http://qa.lzu.edu.cn:8081`.

## Usage

As long as you enter your account and password on the start page of the program, and click login, the program will automatically do the course evaluation job.

![](login.png)

The program will automatically give each teacher the highest feedback, and fill "好" in the text that needs to be filled in.

If the number of teachers of the course is more than 3, the program will evaluate the course first and then the teacher.

**Note:** If you encounter the problem that some teachers are skipped, it may be caused by the network condition. It is recommended to run the programme again.

## Links

* [LZU Auto Course Evaluation Feedback Script](LZU-Auto-Course-Evaluation-Feedback.py)

Tested on 2021-11-12, 2021/22 Mid-term Course Evaluation of the First Semester.

**Warning**:

***For TESTING ONLY, not for any ILLIGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***
