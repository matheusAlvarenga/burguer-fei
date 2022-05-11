from printers.mainmenu import renderMainMenu

def main():
    selected = None

    while(selected != '0'):
        selected = renderMainMenu()
    
if __name__ == "__main__":
    main()