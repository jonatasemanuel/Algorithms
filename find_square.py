#@staticmethod
def check_int(user_input):
    try:
        if isinstance(user_input, int):
            return user_input
    except ValueError:
        print('Please insert a integer number ')
        return False
    # finally:
    #     # colocar em outro validador aqui é so provisorio.
    #     cont = print(input('Continue[ yes / no ]: '))
    #     if cont == 'yes':
    #         pass
    #     else:
    #         return None
                

def square_root(find_root, begin=0, end=None):

    if check_int(find_root):
        # reduizir operaçoes para nao criar lista, e sim checar no mo
        arr = [x for x in range(0, find_root)] 
        # vou ?
        if end is None:
            end = len(arr) - 1
        
        if begin <= end:
            mid = (begin + end) // 2
            if (mid * mid) == find_root:
                return mid
            elif (mid * mid) < find_root:
                return square_root(find_root, mid+1, end)
            else:
                return square_root(find_root, begin, mid-1)
    
    # else:
    #     return "It's Not a number."   
        # precisa tirar daqui para nao ficar validação junto da logica/
        #algoritmos principal
    return None


# MAIN

# colocar print na funcao.
print('\n Square Root: ', square_root(81)) # 1milhao é maximo

# Criar classes para usar OOP.
# Melhorar validação.

# 1º de tudo é arrumar a validação, 
# depois arruma o resto da zona.