def return_vocali(word):
    vocali = ['a', 'e', 'i', 'o', 'u']
    return [let for let in word if let.lower() in vocali]

if __name__ =='__main__':
    word = input('Inserisci una parola... ')
    vocali = return_vocali(word)
    print('La parola {0} contiene {1} vocali'.format(word, len(vocali)))