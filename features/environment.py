import os
import json
import time

from appium import webdriver


def before_scenario(context, scenario):
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'capabilities.json')
    with open(config_file_path) as config_file:
        CONFIG = json.load(config_file)
    desired_capabilities = CONFIG['capabilities']
    CONFIG['capabilities']['app'] = os.path.join(os.path.dirname(__file__), '..', 'utils', 'Hews.apk')
    context.driver = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://localhost:4723/wd/hub"
    )
    time.sleep(9)


def after_scenario(context, scenario):
    if "network" in scenario.tags:
        context.execute_steps('''
        When I enable the network connection
        ''')
    context.driver.quit()
