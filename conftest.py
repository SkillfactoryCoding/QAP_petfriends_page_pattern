import pickle
import uuid

import chromedriver_autoinstaller
import pytest
from selenium import webdriver

from pages.auth_page import AuthPage

chromedriver_autoinstaller.install()


@pytest.fixture
def add_cookies_to_file():
    browser = webdriver.Chrome()
    browser.set_window_size(1400, 1000)

    page = AuthPage(browser)
    page.email.send_keys('delich@gmail.com')
    page.password.send_keys("12345")
    page.btn.click()

    # Save cookies of the browser after the login
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(browser.get_cookies(), cookies)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request):

    browser = webdriver.Chrome()
    browser.maximize_window()

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:

        browser.execute_script("document.body.bgColor = 'white';")

        # Make screen-shot for local debug:
        browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        # For happy debugging:
        print('URL: ', browser.current_url)
        print('Browser logs:')
        for log in browser.get_log('browser'):
            print(log)
