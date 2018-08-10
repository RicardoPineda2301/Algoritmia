lista = [3,39,61,91,57,22,75,89,9,90,63,78,28,73,20]

def MergeSort(lista):
    contador = 0
    if len(lista)>1:
        mid = len(lista)//2
        L = lista[:mid]
        R = lista[mid:]
        MergeSort(L)
        MergeSort(R)
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                lista[k]=L[i]
                i=i+1
            else:
                lista[k]=R[j]
                j=j+1
            k=k+1
            contador = contador + 1
            print(contador)
        while i < len(L):
            lista[k]=L[i]
            i=i+1
            k=k+1
        while j < len(R):
            lista[k]=R[j]
            j=j+1
            k=k+1

print("antes de ordenar: ")        
print(lista)   
MergeSort(lista)
print("luego de ordenar: ")
print(lista)