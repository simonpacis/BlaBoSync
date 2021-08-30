from common import *

def main():
    mainconfig = dict(config.items('main'))
    panelstring = "[bold]Please select the value you want to change:[/bold]\n\n0: Exit"
    i = 1
    for key in mainconfig:
        if key == "password":
            panelstring = panelstring + "\n" + str(i) + ": " + key + " = hidden"
        else:
            panelstring = panelstring + "\n" + str(i) + ": " + key + " = " + mainconfig[key]
        i = i + 1
    panel = Panel(panelstring)
    console.print(panel)
    choice = input("> ")
    if choice == "0":
        quit_prog()
        return True

    if list(mainconfig)[int(choice)-1] == "encrypted":
        console.print("You cannot edit this value. Please change the password to set encryption status of your password.")
        main()
    elif list(mainconfig)[int(choice)-1] == "password":
        print(Panel("Would you like to encrypt the password for your Blackboard installation? This requires you to enter an encyption key that only you know, and that you must type in every time you run BlaBoTool. Type y for yes, or n for no."))
        password = input("> (y/n ")
        if password == "y":
            print(Panel("Please enter the password for your Blackboard installation."))
            password = input("> ")
            print(Panel("Please enter the desired encryption key for your Blackboard installation. You need to type this every time you start BlaBoTool."))
            key = input("> ")
            password = str(encode(key, password))
            config.set('main', 'encrypted', 'True')
        else:
            print(Panel("Please enter the password for your Blackboard installation."))
            password = input("> ")
            config.set('main', 'encrypted', 'False')
        config.set('main', 'password', password)
    else:
        console.print("Please enter the new value.")
        value = input("> ")
        config.set('main', list(mainconfig)[int(choice)-1], value)
    writeConfig()
    readConfig()
    main()
