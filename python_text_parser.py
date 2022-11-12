import re

def reverse_string(_str):
    print(_str[::-1].capitalize() )

def substitute_vowel(_str, new_vowel):
    _str = re.sub(r'[aeiou]', new_vowel, _str)
    print(_str )
    

while 1==1:
    print("1 >> invertir texto")
    print("2 >> sustituir vocal")
    option = input("Seleccione opción: ")

    match option:
        case "1":
            reverse_string(input("Introducir texto: "))
        case "2":
            substitute_vowel(input("Introducir texto: "), input("¿Que vocal desea usar? "))
        