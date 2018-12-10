def get():
    try:
        a = input('请输入第一个数:\n')
        a = float(a)

        c = input('请输入运算符+、-、*、/：\n')
        if c not in ['+', '-', '*', '/']:
            'df' * 'df'
            
        b = input('请输入第二个数:\n')
        b = float(b)

        if c is '+':
            print('结果为', a+b)
            print()

        elif c is '-':
            print('结果为', a-b)
            print()

        elif c is '*':
            print('结果为', a*b)
            print()

        elif c is '/':
            print('结果为', a/b)
            print()

    except ZeroDivisionError:
        print('被除数不能是零\n')

    except ValueError:
        print('你输入的值有问题\n')

    except TypeError:
        print('你输入的运算符有问题\n')
            
if __name__ == '__main__':
    while True:
        d = input("准备运算，按'y'继续，按'q'退出\n")
        if d == 'y':
            get()
        elif d == 'q':
            print('吃饭吧，别算了。')
            break
        else:
            print('输入的不对，从新来\n')
