expression_list = ['我不是', '我没有', '别瞎说']
target_list = []

print('\n否认三连:')

for target in expression_list:
    if target == '别瞎说':
        continue
    print(target)
    target_list.append(target)
else:
    print('\n我是target_list:', target_list)

