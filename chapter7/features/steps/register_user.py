#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
#注意是切换到chapter7目录下运行behave，所以工程目录是#D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter7
#而不是D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython
from features.lib.page.register_page import RegisterPage
from behave import *
use_step_matcher('re')  #表示使用正则表达式


@When('I open the register website "([^"]*)"')
def step1(context,url):
    RegisterPage(context).getUrl(url)

@Then('I expect that the title is "([^"]*)"')  #表示匹配任意字符
def step2(context,expectTitle):
    title = RegisterPage(context).getTitle()
    assert expectTitle in title

@When('I set with email "([^"]*)"')
def step3(context,email):
    RegisterPage(context).sendEmail(email)

@When('I set with username "([^"]*)"')
def step4(context,username):
    RegisterPage(context).sendUsername(username)

@When('I set with password "([^"]*)"')
def step5(context,password):
    RegisterPage(context).sendPassword(password)

@When('I set with code "([^"]*)"')
def step6(context,code):
    RegisterPage(context).sendCode(code)

@When('I click with register_button')
def step7(context):
    RegisterPage(context).clickRegisterButton()

@Then('I expect that text "([^"]*)"')
def step8(context,expectInfo):
    actualInfo = RegisterPage(context).getCodeErrorInfo()
    assert actualInfo == expectInfo