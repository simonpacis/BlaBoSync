#!/usr/local/bin/python3

import requests, json, rich, time, os, shutil, sys, re

from rich.console import Console
from rich.progress import track
from rich.prompt import Prompt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from markdownify import markdownify

console = Console()

with open('CREDENTIALS.json') as json_file:
    data = json.load(json_file)
    username = data['username']
    password = data['password']

with open('COURSES.json') as json_file:
    courses = json.load(json_file)

main_url = "https://abdn.blackboard.com"
login_form_url = "/webapps/login/"

options = Options()
options.headless = True
options.add_experimental_option( "prefs", {'plugins.always_open_pdf_externally': True, 'download.default_directory': os.path.expanduser('~') + "/Downloads/blabotmp"})
driver = None
download_dir = os.path.expanduser('~') + "/Downloads/blabotmp"

def url(url):
    if "http" in url or "https" in url:
        return url
    else:
        return main_url + url

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', str(raw_html))
  return cleantext

def login():
    driver.get(main_url)
    usernamefield = driver.find_element_by_id('user_id')
    passwordfield = driver.find_element_by_id('password')
    usernamefield.send_keys(username)
    passwordfield.send_keys(password)
    loginbutton = driver.find_element_by_id('entry-login')
    loginbutton.click()
    return True 

def movefiles(course_download_dir):
    files = os.listdir(download_dir) 
    files = [x for x in files if not x.startswith(".")]
    console.print("Moving files from temporary directory.", style="white")
    is_crdownload = any("crdownload" in string for string in files)
    while is_crdownload == True:
        files = os.listdir(download_dir) 
        files = [x for x in files if not x.startswith(".")]
        is_crdownload = any("crdownload" in string for string in files)
    i = 0
    for file in files:
        shutil.move(download_dir + "/" + files[i], course_download_dir + "/" + files[i])
        i = i + 1

def create_shortcut(url, course_download_dir, title):
    f = open(course_download_dir + "/" + title +".url", "w")
    f.write("[InternetShortcut]\nURL="+url)
    f.close()
    return True

def create_markdown(title, body, course_download_dir):
    f = open(course_download_dir + "/" + title +".md", "w")
    f.write("# " + title + "\n   \n" + markdownify((body)))
    f.close()
    return True

def get_course(course_url, course_download_dir):
    driver.get(url(course_url))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find(id='crumb_1').contents[0].strip()
    console.print("Getting course materials of course \"" + title + "\"", style="bold white")
    listcontainer = soup.find(id='content_listContainer')
    folders = listcontainer.findChildren("li" , recursive=False)
    for folder in folders:
        folder_anchor = folder.find('a')
        folder_url = url(folder_anchor['href'])
        folder_title = folder_anchor.find('span').contents[0]
        folder_title = "".join(x for x in folder_title if x.isalnum() or x in "._- ")
        folder_title = " ".join(folder_title.split()).title()
        console.print("Download files for unit: \"" + folder_title + "\"", style="bold white")
        folder_dir = course_download_dir + "/" + folder_title
        if os.path.exists(folder_dir) == True:
            shutil.rmtree(folder_dir)
        os.mkdir(folder_dir)
        driver.get(folder_url)
        folder_soup = BeautifulSoup(driver.page_source, 'html.parser')
        folder_listcontainer = folder_soup.find(id='content_listContainer')
        files = folder_listcontainer.findChildren('li', recursive=False)
        for file in track(files, description="Downloading " + str(len(files)) + " files..."):
            file_parent = file.find('h3')
            try:
                anchor = file_parent.find('a')
                if anchor != None:
                    if "panopto" not in anchor['href']:
                        driver.get(url(anchor['href']))
                    else:
                        create_shortcut(anchor['href'], folder_dir, cleanhtml(anchor.contents[0]))
                else:
                    attachments = file.find_all('ul', class_='attachments')
                    anchors = file.find_all('a')
                    for anchor in anchors:
                        if "bbcswebdav" in anchor['href']:
                            driver.get(url(anchor['href']))
                    attachments_title = file.find('h3')
                    attachments_title = attachments_title.get_text(' ', strip=True)
                    attachments_body = file.find('div', class_='details')
                    attachments_body = attachments_body.get_text(' ', strip=True)
                    create_markdown(attachments_title, attachments_body, folder_dir)
            except Exception as e:
                console.print(e)
        files = os.listdir(download_dir)
        files = [x for x in files if not x.startswith(".")]
        while len(files) > 0:
            movefiles(folder_dir)
            files = os.listdir(download_dir)
            files = [x for x in files if not x.startswith(".")]


def main():
    global driver
    console.rule("[bold green]Welcome to BlaBoSync")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    if os.path.exists(os.path.expanduser('~') + "/Downloads/blabotmp") == False:
        os.mkdir(os.path.expanduser('~') + "/Downloads/blabotmp")
    else:
        shutil.rmtree(os.path.expanduser('~') + "/Downloads/blabotmp")
        os.mkdir(os.path.expanduser('~') + "/Downloads/blabotmp")
    with console.status("Logging in as "+username+"...", spinner="growVertical"):
        login()
    i_course = 1
    for course in courses:
        get_course(course['url'], course['download_dir'])
        i_course = i_course + 1

console.print("", style="bold green")
main()
console.print("", style="bold green")

