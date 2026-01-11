import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """Добавление пользовательских параметров для запуска тестов."""
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        choices=['chrome', 'firefox'],
        help="Choose browser: 'chrome' or 'firefox'"
    )
    parser.addoption(
        '--language', action='store', default='ru',
        help="Choose browser language (e.g., 'en', 'ru', 'es'). Default: 'ru'"
    )
    parser.addoption(
        '--headless', action='store_true', default=False,
        help="Run browser in headless mode (no GUI)."
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации и завершения работы браузера."""
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    is_headless = request.config.getoption('headless')

    if browser_name == 'chrome':
        print(f'\nStarting chrome browser with language: {user_language}...')
        options = ChromeOptions()
        options.add_experimental_option('prefs', {
            'intl.accept_languages': user_language,
        })
        if is_headless:
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        
        # Selenium 4.6+ автоматически управляет драйвером через Selenium Manager
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print(f'\nStarting firefox browser with language: {user_language}...')
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        if is_headless:
            options.add_argument('-headless')
        
        # Selenium 4.6+ автоматически управляет драйвером через Selenium Manager
        browser = webdriver.Firefox(options=options)
    else:
        # Защитная проверка (не должна сработать из-за choices в addoption)
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    # Устанавливаем неявные ожидания для стабильности тестов
    browser.implicitly_wait(10)
    
    yield browser
    
    print('\nQuitting browser...')
    browser.quit()