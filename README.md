# BlaBoTool 
My university uses Blackboard to share files, discussions etc.
As I spend 90% of my time in the CLI, I had an idea for a CLI Blackboard tool.
The idea behind BlaBoTool is to be able to control and use different aspects of Blackboard through CLI.
For now, only BlaBoSync exists, which automatically downloads course material to your local computer.

## Installation
Download the following requirements using pip: selenium, markdownify, requests, beautifulsoup4, rich

### Installing selenium
Follow these directions to make sure Selenium is installed correctly.
BlaBoTool uses the chromedriver.
[https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)

## Run BlaBoTool 
Run python3 tool.py, and BlaBoTool will guide you through the setup process.

## Headless mode
You can launch a particular module in BlaBoTool straight from the command line, skipping the main menu altogether; running it headless.
 
This is useful if you're e.g.
running BlaBoSync daily through cron.
Simply pass the import name of the module you want to skip straight to as the first argument when you run tool.py.
To find the import name, go to the top of tool.py and find it in the list called "modules".
So, for BlaBoSync you would launch the tool as such:
  
python3 tool.py sync  
  
And you would skip the main menu.
Please note that in case of encrypted password you do need to manually enter the decryption key in the main menu, but after entering it you will go to the selected module.

Also note that some of the modules allow you to pass an argument to them.
This will be passed as a string to the main function of that module, and is entered as the second argument.
