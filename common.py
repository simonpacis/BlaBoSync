import requests, json, rich, time, os, shutil, sys, re, configparser, base64, importlib, imp
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

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


def url(url):
    global main_url
    if "http" in url or "https" in url:
        return url
    else:
        return main_url + url


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dynamic_imp(name):
    try:
        fp, path, desc = imp.find_module(name)
    except ImportError:
        print ("module not found: " + name)
    try:
        example_package = imp.load_module(name, fp,
                                          path, desc)

    except Exception as e:
        print(e)
    return example_package 

def quit_prog(message = False, clear = False):
    if message:
        console.print("Please restart BlaBoTool for changes to take effect.")
    if clear:
        clear()
    driver.quit()
    sys.exit(0)

def login(passw):
    driver.get(config.get('main', 'main_url'))
    usernamefield = driver.find_element_by_id('user_id')
    passwordfield = driver.find_element_by_id('password')
    usernamefield.send_keys(username)
    passwordfield.send_keys(passw)
    loginbutton = driver.find_element_by_id('entry-login')
    loginbutton.click()
    return True 

def writeConfig():
    global config
    with open('config.ini', 'w') as f:
        config.write(f)

def readConfig():
    global config
    config.read('config.ini')



def common_main():
    global console, config, options, driver, set_clear, main_url, login_form_url, last_ran, username, password, decrypted, logged_in, courses

    config = configparser.ConfigParser()

    if not os.path.isfile('config.ini'):
        shutil.copyfile('config_bak.ini', 'config.ini')

    console = Console()

    options = Options()
    options.headless = True
    options.add_experimental_option( "prefs", {'plugins.always_open_pdf_externally': True, 'download.default_directory': os.path.expanduser('~') + "/Downloads/blabotmp"})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    set_clear = True

    readConfig()

    main_url = config.get('main', 'main_url')
    login_form_url = config.get('main', 'login_form_url')

    if config.get('main', 'last_ran') == "0":
        last_ran = "Never ran"
    else:
        last_ran = str(datetime.fromtimestamp(int(config.get('main', 'last_ran'))))
    config.set('main', 'last_ran', str(int(time.time())))

    username = config.get('main', 'username')
    password = config.get('main', 'password')

    decrypted = False
    logged_in = False
    courses = []

    writeConfig()

common_main()
