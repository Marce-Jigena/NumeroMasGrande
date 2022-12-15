def biggest(lista):
    big_num = lista[0]
    for i in lista:
        if i > big_num:
            big_num = i
    return big_num

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10000, 10, 200000, 11]
print ("El numero mas grtande es:", biggest(lista))