import re
import pprint

def reverse_string(_str):
    print(_str[::-1].capitalize() )

def substitute_vowel(_str, new_vowel):
    _str = re.sub(r'[aeiou]', new_vowel, _str)
    print(_str )
    
def count_words(_str, inverse = False):
    _str_list = _str.split(" ")
    if inverse == True:
        reverse_sentence(_str_list)
    return len(_str_list)

def count_char(_str):
    char_dic = {}
    chars = 0
    for char in _str:
        if char.isalpha():
            chars += 1
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1              
    print("El texto introducido tiene "+ str(chars) + " carácteres")
    for char, valor in char_dic.items():
        print(f'La letra {char} aparece {valor} veces')
    return char_dic, chars

def reverse_sentence(_str):
    _str.reverse()
    _str = " ".join(_str)
    print(_str)
        
    
while 1==1:
    print("1 >> invertir texto")
    print("2 >> sustituir vocal")
    print("3 >> contar carácteres")
    print("4 >> contar palabras")
    print("5 >> buscar palabra en texto")
    print("6 >> invertir palabras")
    option = input("Seleccione opción: ")

    match option:
        case "1":
            reverse_string(input("Introducir texto: "))
        case "2":
            _str = input("Introducir texto: ")
            new_vowel = input("¿Que vocal desea usar?")
            while new_vowel not in ['a', 'e', 'i', 'o', 'u']:
                 new_vowel = input("¿Que vocal desea usar?")
            substitute_vowel(_str, new_vowel)
        case "3":
            text = input("Introduzca un texto: \n ").lower()
            count_char(text)
        case "4":
            text = input("Introduzca una frase: \n ")
            print("La frase introducida tiene "+ str(count_words(text)) + " palabras")
            print(f'la primera letra es "{text[0]}", la última letra es "{text[-1]}"')
        case "5":
            word = input("¿Qué palabra desea buscar? \n ").lower()
            text = input("Introduzca el texto en el que desea encontrar la palabra \n ").lower()
            if word in text:
                print("La palabra SÍ se encuentra en el texto")
            else:
                print("La palabra NO se encuentra en el texto")
        case "6":
            text = input("Introduzca una frase: \n ")
            count_words(text, True)
        case _:
            print("Debe seleccionar una de las opciones numéricas del menú.")