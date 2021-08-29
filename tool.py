from common import *
import sync
import setup

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

        righthand_panel = Panel("[bold]Please select your desired operation from the list below:[/bold]\n\n0: Exit\n1: Modify configuration file\n2: Download course materials (BlaBoSync)")

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

    if prompt == "0":
        clear()
        sys.exit(0)
    elif prompt == "1":
        console.print("Not implemented yet.")
        set_clear = False
    elif prompt == "2":
        sync.main()
    else:
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

if not main_url == "none":
    main()
else:
    setup_screen()

