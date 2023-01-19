# Scrivere una funzione che prenda in ingresso una lista di numeri e in output ritorni la sequenza ordinata dal numero più piccolo al più grande.
#  rimuovere dalla lista eventuali duplicati

def my_sorting(elements):
    sorted_list = []
    current_max = 0
    
    for i in range(len(elements)):
        if elements[i] >= current_max or len(sorted_list) == 0:
            sorted_list.append(elements[i])
            current_max = elements[i]
            continue
        
        for j in range(len(sorted_list)-1, -1, -1):
            if elements[i] > sorted_list[j]:
                
                if elements[i] in sorted_list:
                    sorted_list.remove(elements[i])
                    
                sorted_list.insert(sorted_list.index(sorted_list[j])+1, elements[i])
                break
            
        if(elements[i] not in sorted_list):
            sorted_list.insert(0, elements[i])
        
    return sorted_list


lista1 = [2, 4, 3, 0, 5, 11, 10]
lista2 = [-100, 24, 21, -49, 12, 9, 4920, 0, 12, 3, 1, 229]

print(my_sorting(lista1))
print(my_sorting(lista2))

# metodo veloce con sort()
lista1.sort()
print(lista1)