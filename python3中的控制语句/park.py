'''
    小明要去逛公园，输入小明的年龄可以得到,公园对小明的优惠政策
'''

def age():
    a = input('请输入小明的年龄\n')
    a = int(a)

    if a<0:
        print('你年龄输入的有问题\n')

    elif a<=10: 
        print('小明免票,并且给小明一个小熊玩具\n')

    elif a<=16:
        print('小明只有免票的待遇\n')

    elif a<=59:
        print('小明要付全票\n')

    elif a>120:
        print('老寿星好\n')

    else:
        print('小明免票，并且可以和老伴免费拍张合影\n')

if __name__ == '__main__':
    while True:
        try:
            q = input('输入q退出，y继续\n')

            if q == 'y':
                age()

            elif q == 'q':
                break

            else:
                print('你没有按要求输入\n')

        except ValueError:
            print('你应该输入数字\n')
