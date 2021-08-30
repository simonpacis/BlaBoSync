from common import *

modules = [
        {"import": "sync", "menu": True, "text": "Download course materials (BlaBoSync)", "clear": True},
        {"import": "configure", "menu": True, "text": "Modify configuration file", "clear": False},
        {"import": "setup", "menu": False}
        ]

for module in modules:
    globals()[module['import']] = dynamic_imp(module['import'])

def main():
    global set_clear, decrypted, password, logged_in, username
    if set_clear == True:
        clear()
        readConfig()

        if config.get('main','encrypted') == "True":
            hidden = "encrypted"
        else:
            hidden = "hidden"

        lefthand_panel = Panel.fit("[bold]Last ran:[/bold] " + last_ran + "\n[bold]Blackboard URL:[/bold] " + config.get('main', 'main_url') +"\n[bold]Login form URL:[/bold] " + login_form_url + "\n[bold]Username:[/bold] " + config.get('main', 'username') + "\n[bold]Password:[/bold] " + hidden, title="Configuration")

        righthand_panel = "[bold]Please select your desired operation from the list below:[/bold]\n"

        i = 1
        for module in (module for module in modules if module['menu']):
            righthand_panel = righthand_panel + "\n" + str(i) + ": " + module['text'] 
            i = i + 1

        righthand_panel = righthand_panel + "\n0: Exit"
        righthand_panel = Panel(righthand_panel)

        panels = [lefthand_panel, righthand_panel]

        columns = Columns(panels, equal=False, expand=False)

        console.rule("[bold green]Welcome to BlaBoTool")
        print(columns)
    else:
        set_clear = True

    if config.get('main','encrypted') == "True" and decrypted == False:
        console.print("Your password is encrypted. Please enter your decryption key.")
        key = Prompt.ask(">")
        password = decode(key, config.get('main', 'password'))
        decrypted = True

    if not logged_in:
        with console.status("Logging in as " + username + "...", spinner="growVertical"):
            login(password)
        logged_in = True
        clear()
        main()

    prompt = Prompt.ask(">") 

    menu_modules = list(module for module in modules if module['menu'])
    if prompt == "0":
        clear()
        driver.quit()
        sys.exit(0)
    else:
        globals()[menu_modules[int(prompt)-1]['import']].main()
        pass
    main()

def setup_screen():
    clear()
    righthand_panel = Panel("Seems like this is the first time you've ever ran BlaBoTool. You have to configure it before first use.\n\n[bold]Please select your desired operation from the list below:[/bold]\n\n0: Exit\n1: Setup")
        
    console.rule("[bold green]Welcome to BlaBoTool")
    print(righthand_panel)
    prompt = Prompt.ask(">")
    if prompt == "0":
        clear()
        sys.exit(0)
    elif prompt == "1":
        setup.main()
    else:
        pass
    readConfig()
    if not config.get('main', 'main_url') == "none":
        main()
    else:
        setup_screen()
try:
    if not config.get('main', 'main_url') == "none":
        main()
    else:
        setup_screen()
except KeyboardInterrupt:
    driver.quit()
