# BlaBoSync 
My university uses Blackboard to share files, discussions etc.
The idea behind BlaBoSync is to scrape the website and download all material for the courses (which are always uploaded as .docx or .pdf) locally, and then when run again, if a file has changed remotely, replace the local file with the new version from Blackboard.

## Installation
Download the following requirements using pip: selenium, markdownify, requests, beautifulsoup4, rich

### Installing selenium
Follow these directions to make sure Selenium is installede correctly.
BlaBoSync uses the chromedriver.
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

Copy the COURSES_blank.json and CREDENTIALS_blank.json to COURSES.json and CREDENTIALS.json, and enter the necessary information.

Run python3 sync.py, and watch BlaBoSync download your stuff.
