from common import *
import sync

def main():
    global set_clear
    if set_clear == True:
        clear()

        lefthand_panel = Panel.fit("[bold]Last ran:[/bold] " + last_ran + "\n[bold]Blackboard URL:[/bold] " + main_url+"\n[bold]Login form URL:[/bold] " + login_form_url, title="Information")

        righthand_panel = Panel("[bold]Please select your desired operation from the list below:[/bold]\n\n0: Exit\n1: Modify configuration file\n2: Download course materials (BlaBoSync)")

        panels= [lefthand_panel, righthand_panel]

        columns = Columns(panels, equal=False, expand=False)

        console.rule("[bold green]Welcome to BlaBoSync")
        print(columns)
    else:
        set_clear = True
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

main()
