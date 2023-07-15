import subprocess
from enum import Enum

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


class SelenoidCommand(str, Enum):
    RUN_SELENOID = '../cm.exe selenoid start'
    RUN_SELENOID_UI = '../cm.exe selenoid-ui start'


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://github.com/", help="Base url")
    parser.addoption("--bro", action="store", default="chrome", help="browser")
    parser.addoption("--bro_version", action="store", default="114.0", help="browser version")
    parser.addoption("--executor", action="store", default="http://localhost:4444/wd/hub", help="Selenoid ip")


def pytest_exception_interact(node):
    driver = node.instance.driver
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope='session', autouse=True)
def start_selenoid():
    run_selenoid_command = subprocess.run(SelenoidCommand.RUN_SELENOID.value,
                                          shell=True,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          encoding='utf-8'
                                          )
    if run_selenoid_command.returncode == 0:
        print('Run selenoid .......')
        print(run_selenoid_command.stdout)
        if "Selenoid is already running" in run_selenoid_command.stdout:
            print("Selenoid is already running")
    else:
        print(f"Error {run_selenoid_command.stderr}")


@pytest.fixture(scope='session', autouse=True)
def start_selenoid_ui():
    run_selenoid_command = subprocess.run(SelenoidCommand.RUN_SELENOID_UI.value,
                                          shell=True,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          encoding='utf-8'
                                          )
    if run_selenoid_command.returncode == 0:
        print('Run selenoid ui.......')
        print(run_selenoid_command.stdout)
    else:
        print(f"Error {run_selenoid_command.stderr}")


@pytest.fixture(autouse=True)
def driver(request):
    base_url = request.config.getoption("--url")
    browser = request.config.getoption("--bro")
    bro_version = request.config.getoption("--bro_version")
    executor = request.config.getoption("--executor")

    capabilities = {
        "browserName": browser,
        "browserVersion": bro_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True
        }
    }

    driver = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=capabilities)
    request.cls.driver = driver
    driver.get(base_url)
    driver.maximize_window()
    yield
    driver.quit()
