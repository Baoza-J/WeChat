def get():
    a = input('请输入第一个数:\n')
    c = input('请输入运算符+、-、*、/：\n')
    b = input('请输入第二个数:\n')


    if c is '+':
        try:
            a = float(a)
            b = float(b)
            print('结果为', a+b)
            print()
        except (ValueError, TypeError):
            print('你输入的有问题\n')

    elif c is '-':
        try:
            a = float(a)
            b = float(b)
            print('结果为', a-b)
            print()
        except (ValueError, TypeError):
            print('你输入的有问题\n')

    elif c is '*':
        try:
            a = float(a)
            b = float(b)
            print('结果为', a*b)
            print()
        except (ValueError, TypeError):
            print('你输入的有问题\n')

    elif c is '/':
        try:
            a = float(a)
            b = float(b)
            print('结果为', a/b)
            print()
        except (ValueError, ZeroDivisionError, TypeError):
            print('你输入的有问题！！！\n')

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
