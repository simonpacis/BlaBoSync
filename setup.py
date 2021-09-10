from common import *

def main():
    global main_url, password, username
    print(Panel("Please configure the root URL of the Blackboard installation you're using. E.g. https://school.blackboard.com."))
    main_url = input("> ")
    config.set('main', 'main_url', main_url)
    print(Panel("Please enter the username for your Blackboard installation. This can be changed later manually in config.ini, if you do not trust typing it directly into the terminal. In that case, please type something arbitrary and change it after."))
    username = input("> ")
    config.set('main', 'username', username)
    print(Panel("Would you like to encrypt the password for your Blackboard installation? This requires you to enter an encyption key that only you know, and that you must type in every time you run BlaBoTool. Type y for yes, or n for no."))
    password = input("> (y/n) ")
    if password == "y":
        print(Panel("Please enter the password for your Blackboard installation."))
        password = input("> ")
        print(Panel("Please enter the desired encryption key for your Blackboard installation. You need to type this every time you start BlaBoTool."))
        key = input("> ")
        password = str(encode(key, password))
        config.set('main', 'encrypted', 'True')
    else:
        print(Panel("Please enter the password for your Blackboard installation. This can be changed later manually in config.ini, if you do not trust typing it directly into the terminal. In that case, please type something arbitrary and change it after."))
        password = input("> ")
        config.set('main', 'encrypted', 'False')
    config.set('main', 'password', password)
    writeConfig()
    readConfig()
    username = config.get('main', 'username')
    password = config.get('main', 'password')
    quit_prog(True)


