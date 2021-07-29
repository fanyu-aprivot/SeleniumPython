#coding=utf-8
Feature: Register User

As a developer
This is my first bdd project

Scenario: open register website
    When I open the register website "http://www.5itest.cn/register"
    Then I expect that the title is "注册"

Scenario: input register info
    When I set with email "12345@qq.com"
    And I set with username "fanyu120"
    And I set with password "123456"
    And I set with code "11111"
    And I click with register_button
    Then I expect that text "验证码错误"