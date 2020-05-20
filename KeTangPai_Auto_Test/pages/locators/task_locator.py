# -*- coding: utf-8 -*-
# @author: yangyd
# @file: task_locator.py
# @time: 2019/8/30 14:20


from selenium.webdriver.common.by import By


class TaskLocator:

    task_locator = (By.XPATH, "//a[text()='作业']")
    home_work_locator = (By.XPATH,
                         "//a[@title='web考核项目来袭！！ 是时候证明自己，没有老师你也是可以的！！！  ']")
    add_file = (By.XPATH, "//input[@name='file']")

    message_locator = (By.XPATH, "//span[@class='s2']")
    msg_input_locator = (By.ID, "comment")
    save_btn = (By.XPATH, "//div[@class='work-message2 clearfix']//a[@class='sure active']")

