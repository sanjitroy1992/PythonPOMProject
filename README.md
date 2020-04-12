Creating a python Page Object Model(POM) is a very good way to create your automation test cases and make a unittest frameowrk built around it.
In this tutorial we are going to learn how to create a simple logoin Test to automate a scenario using POM.

Step by Step:

We will do this hands-on:
1. Create a simple login test
2. Implement unit testing
3. Implement Page Object Model
4. Separate test scripts and objects
5. Create a separate class for Locators
6. Run from command line
7. Add HTML Reports
	
1. use python selenium webdriver to create a simple login test.
2. In order to conver a test to a unittest do the following steps.
 - import unittest
 - create a class with as below passing unittest Testcases module ->class LoginPage(unittest.Testcase)
 - create a setUpClass method which will be initialized at the beginning of tests. One thing to remember when you are usign a class function always provide the anotation at classmethod.
  @classmethod
  def setUp(self):
 - create a tearDownClass method which will be called at the end of all the tests. like setUpClass method provide the anotation at classmethod for tearDownClass.
  @classmethod
  def tearDown(self):
 - To create test cases make sure to name it starting with 'test'. As an example: test_login_page(self):
   'test' is to tell unittest that it is a test case.
	   
