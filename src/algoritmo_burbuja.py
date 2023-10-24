def algoritmo_burbuja(arr):
    n = len(arr)
    print(f'Estado inicial: {arr}')
    for i in range(n-1):
        #Inicializamos una variable para verificar si se hizo algun intercambio en este recorrido
        intercambio = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambio = True
                print(f'{arr}')
        #Si no se hizo ningun intercambio en este recorrido, la lista ya está ordenada
        if not intercambio:
            print(f'La lista esta completamente ordenada. No se necesitan mas iteraciones.')
            return

if __name__ == "__main__":
    
    a = [8, 3, 1, 19, 14]
    algoritmo_burbuja(a)