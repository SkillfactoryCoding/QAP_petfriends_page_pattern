from pages.petfriends import MainPage


def test_download_cookies(add_cookies_to_file):
    """
    Вызывается один раз, чисто для того, чтобы скачать куки с сайта и записать их в файл "my_cookies.txt",
    для того чтобы далее использовать в тестах.
    Тест пустой, так как в нем нет никакой логики, вся логика реализована в фикстуре,
    он нужен чисто для разового прогона фикстуры.
    """
    pass


def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """

    page = MainPage(web_browser)

    # Scroll down till the end using actionchains and click on the last image
    page.scroll_down()

    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')
