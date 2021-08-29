# BlaBoTool 
My university uses Blackboard to share files, discussions etc.
The idea behind BlaBoTool is to be able to control and use different aspects of Blackboard through CLI.
For now, only BlaBoSync exists, which automatically downloads course material to your local computer.

## Installation
Download the following requirements using pip: selenium, markdownify, requests, beautifulsoup4, rich

### Installing selenium
Follow these directions to make sure Selenium is installed correctly.
BlaBoSync uses the chromedriver.
[https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)

Copy the COURSES_blank.json and CREDENTIALS_blank.json to COURSES.json and CREDENTIALS.json, and enter the necessary information.

Run python3 tool.py, and watch BlaBoSync download your stuff.

