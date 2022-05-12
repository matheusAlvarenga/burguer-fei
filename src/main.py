from printers.mainmenu import renderMainMenu
from services.user import signIn
from utils.clear_terminal import clear


def main():
    selected = None

    while(selected != '0'):
        clear()
        selected = renderMainMenu()

        if(selected == '1'):
            user = signIn()
            if(not user):
                clear()
                print('Já existe um usuário com esse CPF!')
                input('Pressione enter para voltar ao menu.')
                continue


if __name__ == "__main__":
    main()
