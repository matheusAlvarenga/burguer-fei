from printers.mainmenu import renderMainMenu
from services.order import createOrder,deleteOrder, deleteProductInOrder, printFullResume, totalPriceFromOrders
from services.user import logIn, signIn
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
            else:
                createOrder(user['document'])

        elif(selected == '2'):
            user = logIn()

            if(not user):
                clear()
                print('Login errado. Tente novamente.')
                input('Pressione enter para voltar ao menu.')
                continue
            else:
                deleteOrder(user['document'])
                input('Pressione enter para voltar ao menu.')
                continue

        elif(selected == '3'):
            user = logIn()

            if(not user):
                clear()
                print('Login errado. Tente novamente.')
                input('Pressione enter para voltar ao menu.')
                continue
            else:
                createOrder(user['document'])

        elif(selected == '4'):
            user = logIn()

            if(not user):
                clear()
                print('Login errado. Tente novamente.')
                input('Pressione enter para voltar ao menu.')
                continue
            else:
                result = deleteProductInOrder(user)
                if(result):
                    clear()
                    print('Produto removido com sucesso')
                input('Pressione enter para voltar ao menu.')
                continue

        elif(selected == '5'):
            user = logIn()

            if(not user):
                clear()
                print('Login errado. Tente novamente.')
            else:
                total_price = totalPriceFromOrders(user)
                clear()
                print('Preço total: R$', total_price)

            input('Pressione enter para voltar ao menu.')
            continue

        elif(selected == '6'):
            user = logIn()

            if(not user):
                clear()
                print('Login errado. Tente novamente.')
            else:
                printFullResume(user)

            input('Pressione enter para voltar ao menu.')
            continue


if __name__ == "__main__":
    main()
