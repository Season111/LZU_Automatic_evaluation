# -*- coding:utf-8 -*-
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLEGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

driver = webdriver.Chrome()

print("请在打开的浏览器界面中登录，之后会自动开始评教！")

driver.get("http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn")
WebDriverWait(driver, 5)

NetworkErr = False
while True:
    if driver.find_element_by_xpath('/html').get_attribute('dir') == "ltr":
        if not NetworkErr:
            print("Network error, please check your network!")
            NetworkErr = True
        driver.get(
            "http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn")
        time.sleep(3)
    else:
        NetworkErr = False
        break

while True:
    time.sleep(3)
    if "http://my.lzu.edu.cn/main" in driver.current_url:
        break

driver.get("http://qa.lzu.edu.cn:8081/loginSSO2")
WebDriverWait(driver, 5)
NetworkErr = False
while True:
    if driver.find_element_by_xpath('/html').get_attribute('dir') == "ltr":
        if not NetworkErr:
            print("Network error, please check your network!")
            NetworkErr = True
        driver.get(
            "http://qa.lzu.edu.cn:8081/loginSSO2")
        time.sleep(3)
    else:
        NetworkErr = False
        break

js = '''return document.querySelector('#task-list').getElementsByTagName('li').length'''
taskList = driver.execute_script(js)

for i in range(1, taskList+1):
    js = '''return document.querySelector('#task-list>li:nth-child(''' + \
        str(i)+''')').className'''
    currentClass = driver.execute_script(js)
    if currentClass == "over":
        continue
    js = '''document.querySelector('#task-list>li:nth-child(''' + \
        str(i)+''')').click()'''
    driver.execute_script(js)
    time.sleep(3)

    js = '''return document.querySelector("#tipDlg > div.modal-footer > button").disabled'''
    while driver.execute_script(js):
        time.sleep(3)
    
    js = '''document.querySelector("#tipDlg > div.modal-footer > button").click()'''
    driver.execute_script(js)
    time.sleep(3)

    js = '''return document.querySelector('#pjkc').rows.length'''
    rows = driver.execute_script(js)

    for j in range(1, rows+1):
        js = '''document.querySelector("#pjkc > tr:nth-child(''' + \
            str(j) + ''') > td:nth-child(3) > div > a").click()'''
        driver.execute_script(js)
        time.sleep(3)

        js = '''return document.querySelector("#sample_2>tbody").getElementsByTagName('tr').length'''
        teachers = driver.execute_script(js)

        if teachers > 3:
            js = '''document.querySelector("#kfxpjDlg > div.modal-header > button").click()'''
            driver.execute_script(js)
            time.sleep(3)

            if driver.execute_script('''return document.querySelector("#pjkc > tr:nth-child(''' + str(j) + ''') > td:nth-child(6)").getElementsByTagName('div').length == 0'''):
                pass
            else:
                js = '''document.querySelector("#pjkc > tr:nth-child(''' + str(
                    j) + ''') > td:nth-child(6) > div > a").click()'''
                driver.execute_script(js)
                time.sleep(3)

                js = '''return document.getElementsByClassName("controls").length'''
                input = driver.execute_script(js)
                time.sleep(3)

                for l in range(3, input-3):
                    js = '''document.getElementsByClassName("controls")['''+str(
                        l)+'''].getElementsByTagName('label')[0].click()'''
                    driver.execute_script(js)

                js = '''
                    document.getElementsByClassName("controls")['''+str(input-3)+'''].getElementsByTagName('label')[1].click();
                    document.getElementsByClassName("controls")['''+str(input-2)+'''].getElementsByTagName('textarea')[0].value = "好";
                    document.getElementsByClassName("controls")['''+str(input-1)+'''].getElementsByTagName('textarea')[0].value = "好";
                    '''
                driver.execute_script(js)
                time.sleep(3)

                js = '''document.querySelector("#pjsubmit").click()'''
                driver.execute_script(js)
                time.sleep(3)

                js = '''document.querySelector("#finishDlg > div.modal-footer > button").click()'''
                driver.execute_script(js)
                time.sleep(3)

            js = '''document.querySelector("#pjkc > tr:nth-child(''' + str(
                j) + ''') > td:nth-child(3) > div > a").click()'''
            driver.execute_script(js)
            time.sleep(3)

            js = '''return document.querySelector("#sample_2>tbody").getElementsByTagName('tr').length'''
            teachers = driver.execute_script(js)
            time.sleep(1)

        for k in range(1, teachers+1):
            time.sleep(0.5)
            js = '''return document.querySelector("#sample_2 > tbody > tr:nth-child('''+str(
                k)+''') > td:nth-child(3) > div > a").className'''
            if (driver.execute_script(js) == "badge badge-success"):
                continue
            js = '''document.querySelector("#sample_2 > tbody > tr:nth-child('''+str(
                k)+''') > td:nth-child(3) > div > a").click()'''
            driver.execute_script(js)
            time.sleep(3)

            js = '''return document.getElementsByClassName("controls").length'''
            input = driver.execute_script(js)
            time.sleep(3)

            for l in range(3, input-3):
                js = '''document.getElementsByClassName("controls")['''+str(
                    l)+'''].getElementsByTagName('label')[0].click()'''
                driver.execute_script(js)

            js = '''
                document.getElementsByClassName("controls")['''+str(input-3)+'''].getElementsByTagName('label')[1].click();
                document.getElementsByClassName("controls")['''+str(input-2)+'''].getElementsByTagName('textarea')[0].value = "好";
                document.getElementsByClassName("controls")['''+str(input-1)+'''].getElementsByTagName('textarea')[0].value = "好";
                '''
            driver.execute_script(js)
            time.sleep(3)

            js = '''document.querySelector("#pjsubmit").click()'''
            driver.execute_script(js)
            time.sleep(3)

            js = '''document.querySelector("#finishDlg > div.modal-footer > button").click()'''
            driver.execute_script(js)
            time.sleep(3)

        js = '''document.querySelector("#kfxpjDlg > div.modal-header > button").click()'''
        driver.execute_script(js)
        time.sleep(3)

    js = '''document.querySelector("#titlelist > div.actions > div > a").click()'''
    driver.execute_script(js)
    time.sleep(3)

driver.close()

print("评教已经结束！请检查是否已经全部评教完成，如果还没有可以多运行几遍本程序。")
