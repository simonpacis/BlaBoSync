import requests, json, rich, time, os, shutil, sys, re, configparser
from datetime import datetime

from rich.console import Console
from rich.progress import track
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
from rich.console import Group
from rich.columns import Columns

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from markdownify import markdownify

config = configparser.ConfigParser()
config.read('config.ini')

console = Console()

options = Options()
options.headless = True
options.add_experimental_option( "prefs", {'plugins.always_open_pdf_externally': True, 'download.default_directory': os.path.expanduser('~') + "/Downloads/blabotmp"})
driver = None
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)

set_clear = True

main_url = config.get('main', 'main_url')
login_form_url = config.get('main', 'login_form_url')
if config.get('main', 'last_ran') == "0":
    last_ran = "Never ran"
else:
    last_ran = str(datetime.fromtimestamp(int(config.get('main', 'last_ran'))))
config.set('main', 'last_ran', str(int(time.time())))

with open('config.ini', 'w') as f:
    config.write(f)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

