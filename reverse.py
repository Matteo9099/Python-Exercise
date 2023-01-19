# funzione che accetta come parametro una stringa e ne ritorna il valore al contrario.

def reverse_string(word):
    return word[::-1]

text = reverse_string('Hello World')
print(text)

text2 = reverse_string('Programming with python!')
print(text2)