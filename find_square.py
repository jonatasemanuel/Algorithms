#staticmethod
def check_int(user_input):

    try:
        if isinstance(user_input, int):
           return True  

    except TypeError:
            if isinstance(user_input, float):
                print('\nPlease insert a integer number \n')
                return False
                
    except SyntaxError:
            print('Just number')
            return False

    
def square_root(find_root, begin=0, end=None):
    
        if check_int(find_root):
        
            arr = [x for x in range(0, find_root)] 

            if end is None:
                end = len(arr) - 1
            
            if begin <= end:
                mid = (begin + end) // 2
                
                if (mid * mid) == find_root:
                    print(f'\n√{find_root} → {mid}\n')
                    return mid
                elif (mid * mid) < find_root:
                    return square_root(find_root, mid+1, end)
                else:
                    return square_root(find_root, begin, mid-1)
            else:
                return print(f'\n√{find_root} → No square root\n')

        # return None


if __name__ == '__main__':

    square_root("teste")
    square_root(81)
    square_root(1.1)
    square_root(11)
    square_root('23fdf') 


# 1º de tudo é arrumar a validação, depois arruma o resto da zona.
# Criar classes para usar OOP.
# colocar print na funcao ou classe
# # Reduizir operaçoes para nao criar lista no list comprehension, 
# e sim checar no momento ?
