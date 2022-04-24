from ntpath import join
lista_hexadecimal = ["0",'1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F"]
#funcao para converter para a base 10 
def conversao_base_10(lista_n,base_n):#lista_n e o numero em lista e base_n a base que o usuario digitou
    soma = 0
    index_lista = len(lista_n)
    for i in lista_n:#percorrendo dentro da lista, para encontrar o elemento e fazer as contas
        aux_inteiro = int(i)#convertendo  o elemento da lista para inteiro, para poder fazer a operacao matematica
        soma += (aux_inteiro * (base_n**(index_lista-1)))
        index_lista -=1
    return soma

def conversao_base_requerida(base_n_desejada,num_base_10):
    lista_resultado_final = [] #lista para armazenar o numero.
    while num_base_10>0: 
        resto_div = num_base_10 %base_n_desejada #resto_div e o resto da divisao do
        num_base_10 = num_base_10//base_n_desejada
        string_resto_div = str(resto_div)#convertendo em string, para depois remover o formato de lista
        lista_resultado_final.append(string_resto_div)
    lista_resultado_final.reverse()#invertvendo a ordem
    lista_resultado_final = "".join(lista_resultado_final)#convertendo a lista em string
    return lista_resultado_final
#convertendo de hexadecimal para base 10
def conversao_hexa_base_10(lista_num):
    num_dec = 0
    auxiliar = len(lista_num)
    for i in lista_num:
        contador = 0#contador para filtrar dentro da lista dos numeros hexadecimal, com objetivo de fazer a operacao
        for j in lista_hexadecimal:
            if j == i:
                num_dec += contador*(16**(auxiliar-1)) #operacao para fazer a conta e transformar o num hexadecimal para base 10
                auxiliar -=1 
            contador +=1
    return num_dec

def conversao_base_dec_hexa(num_dec):
    lista_num_hexa_final = [] 
    while num_dec >0: #enquanto o numero na base decimal for maior que zero
        resto_div = num_dec % 16
        num_dec = num_dec//16
        numero_hexa = lista_hexadecimal[resto_div]
        string_numero_hexa = str(numero_hexa) #transformando em string para depois remover do formato da lista
        lista_num_hexa_final.append(string_numero_hexa)
    lista_num_hexa_final.reverse()#invertendo a ordem, já que o resto e do ultimo ao primeiro
    lista_num_hexa_final = "".join(lista_num_hexa_final)#convertendo a lista em string
    return lista_num_hexa_final

numero = input("Digite o numero: ")
numero = numero.upper()
base = int(input("Digite a base desse numero: "))
base_desejada = int(input("Digite a base para qual deseja converter: "))
lista_numero = list(numero)


if (base>=2 and base <=10) or (base == 16):
    if (base==16):
        resultado_hex_dec = conversao_hexa_base_10(lista_numero)#convertendo de hexadecimal para base 10
        resultado_hex_base_desejada = conversao_base_requerida(base_desejada,resultado_hex_dec)
        print(f"O numero {numero} na base 16 e igual a {resultado_hex_base_desejada} na base {base_desejada}")
        
    elif (base!=10):
        if base_desejada==16:# se a base desejada for 16, faremos um metodo diferente de conversao, por isso esse if
            resultado_conversao_base_10 = conversao_base_10(lista_numero,base)
            resultado_final = conversao_base_dec_hexa(resultado_conversao_base_10)
            print(f"O numero {numero} na base {base} e {resultado_final} na base 16 ")
        else:
            resultado_conversao_base_10 = conversao_base_10(lista_numero,base)
            resultado_final = conversao_base_requerida(base_desejada,resultado_conversao_base_10)
            print(f"O numero {numero} na base {base} e {resultado_final} na base {base_desejada}")

    else:
        if base_desejada==16:# se a base desejada for 16, faremos um metodo diferente de conversao, por isso esse if
            resultado_conversao_base_10 = conversao_base_10(lista_numero,base)
            resultado_final = conversao_base_dec_hexa(resultado_conversao_base_10)
            print(f"O numero {numero} na base {base} e {resultado_final} na base 16 ")
        else:
            numero = int (numero) # se a base ja for 10, nao precisamos converter o num para a base 10, apenas para a desejada
            resultado_final = conversao_base_requerida(base_desejada,numero)
            print(f"O numero final e {resultado_final}")
else:
    print("Base incorreta.")

