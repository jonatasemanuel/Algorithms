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
            if end is None:
                end = find_root // 2

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

        return None


if __name__ == '__main__':

    square_root(1000000000000)
    square_root(16)