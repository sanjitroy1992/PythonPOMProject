import os
import inspect


class TestData:
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    FIREFOX_EXECUTABLE_PATH = parentdir + "\Drivers\geckodriver.exe"
    HTML_Report_Path = parentdir + "\Reports"
    App_Url = 'https://opensource-demo.orangehrmlive.com/'
    Username = 'Admin'
    Invalid_Username = 'Admin1'
    Password = 'admin123'
    Invalid_Credentials = 'Invalid credentials'