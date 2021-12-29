# 兰州大学自动评教
ps：项目原作者为HOLLOMAN

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/LZU-Auto-Course-Evaluation-Feedback)](../../graphs/commit-activity)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/LZU-Auto-Course-Evaluation-Feedback?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/LZU-Auto-Course-Evaluation-Feedback?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/LZU-Auto-Course-Evaluation-Feedback?style=social)](../../network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/LZU-Auto-Course-Evaluation-Feedback.svg)](../../archive/master.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/LZU-Auto-Course-Evaluation-Feedback.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/LZU-Auto-Course-Evaluation-Feedback/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/LZU-Auto-Course-Evaluation-Feedback.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/LZU-Auto-Course-Evaluation-Feedback/context:python)

(English version is down below)

[Python库依赖](../../network/dependencies)

此程序使用Python的selenium库，使用前请确保电脑上已经安装了Google Chrome浏览器，并且在程序执行目录下放置了[Chrome Driver](https://chromedriver.chromium.org)

此程序适用于 `http://qa.lzu.edu.cn:8081` 页面的评教。

## 使用方法

只要在程序运行开始的页面输入你的账号和密码，并点击登录，程序将会自动为你评教。

![](login.png)

程序会自动为每个老师给予最高的评价，并在需要填写文字处填写上“好”。

如果该课程老师数量大于3个，程序会首先进行课程的评教，再进行老师的评教。

**注：**：如果遇到有的老师被跳过的问题，可能是由网络状况引起的，建议再次运行一下。

## 链接

* [兰州大学自动评教 脚本](LZU-Auto-Course-Evaluation-Feedback.py)

测试于2021年11月12日, 2021-2022学年第一学期期中评教。

ps：项目原作者为HOLLOMAN

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
