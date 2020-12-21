def filename():
    with open('file1.txt') as f1:
        list1=f1.read().splitlines()
    with open('file2.txt') as f2:
        list2=f2.read().splitlines()
    file_list=list(set(list1)-set(list2))
    for name in file_list:
        print(name.split('.')[0])

filename()