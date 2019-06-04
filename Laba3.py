import os


def number_files():
    name = input("Введите путь:")
    files = next(os.walk(name))
    print(len(files) - 1)


def products():
    global list1
    list1 = []
    j = 1
    with open('products.txt', 'r') as f:
        list2 = [line.strip().split(';') for line in f]
    for i in list2:
        if int(i[2]) > 1700:
            list1.append(i)
    for i in list1:
        del i[0]
    list1.sort()
    print("№,Наименование товара,Цена,Количество")
    for i in list1:
        i.insert(0, str(j))
        print(i)
        j += 1


def products2():
    products()
    number = input("Укажите номера товаров, у которых нужно уменьшить цену через пробел : ").split()
    cost = int(input("На сколько уменьшить цены? : "))
    for i in list1:
        if i[0] in number:
            i[2] = int(i[2]) - cost
        print(i)


def products3():
    products2()
    file = open(input("Введите путь к файлу, в который сохранить данные: "), 'w')
    for i in list1:
        file.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]) + '\n')
    file.close()


while True:

    while True:

        x = int(input("Введите число, нужной функции :"))

        if x == 1:
            number_files()
            break
        elif x == 2:
            products()
            break
        elif x == 3:
            products2()
            break
        elif x == 4:
            products3()
            break
        else:
            print('Некорректный ввод')

    y = input('Вы хотите продолжить? :')

    if y == '0' or y == 'no' or y == 'N' or y == 'нет' or y == 'No' or y == 'Нет' or y == 'n':
        break

    if y == '1' or y == 'yes' or y == 'Y' or y == 'да' or y == 'Yes' or y == 'Да' or y == 'y':
        continue

    else:
        print('Некорретный ввод')
        break
