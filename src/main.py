from printers.mainmenu import renderMainMenu
from services.user import signIn


def main():
    selected = None

    while(selected != '0'):
        selected = renderMainMenu()

        if(selected == '1'):
            user = signIn()
            if(not user):
                print('Já existe um usuário')


if __name__ == "__main__":
    main()
