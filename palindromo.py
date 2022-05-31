
def palindromo(palavra):
    return str(palavra) == str(palavra)[::-1]
palavra = input("Digite uma palavra: ")
if palindromo(palavra):
    print(palavra, "é palíndromo")
else:
    print(palavra, "não é palíndromo")


