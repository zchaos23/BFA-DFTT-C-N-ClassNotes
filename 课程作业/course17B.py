with open("dict.txt", 'r', encoding='utf-8') as f:
    my_dict = {}
    source = f.read()
    lines = source.split('\n')
    for line in lines[:-1]:
        print(line)
        en = line.split('   ')[0]
        print(type(en))
        cn_with_p = line.split('   ')[1].split(',')
        cn = cn_with_p[0].split('.')[1].split('，')
        my_dict[en] = cn

with open("dict.txt", 'w', encoding='utf-8') as f:
    outputs = ''
    for word in list(my_dict.keys()):
        outputs += ('{}:{}\n'.format(word, ','.join(my_dict[word])))
    f.write(outputs)
