expression_list = ['我不是', '我没有', '别瞎说']
target_list = []

print('\n否认三连:')

for target in expression_list:
    if target == '别瞎说':
        break
    print(target)
    target_list.append(target)
else:
    print('\n我是target_list:', target_list)

print('\n对循环外的我没有影响,我来打印 target_list:\n', target_list)

