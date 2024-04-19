encontrar=[]
costo=[]
contado=[]
suma=0
Flag=True 

while Flag is True:
    piezaz = int(input('Cuantas piezaz necesitas encontrar: '))
    encontrar.append(piezaz)
    valor = float(input('Costo del producto: $'))
    costo.append(valor)
    while contado != encontrar:
        buscar = int(input('Piezas encontradas: '))
        contado.append(buscar)
        for i in contado:
            suma=sum(contado)
            print(f'Tu conteo {contado}')
            print(f'Total contado {suma}')
        if suma >= encontrar[0]:
            termina=str(input('Has encontrado todas las piezas deces terminar (s/n)'))
            if termina=='s':
                print(f'Encontraste {suma} piezas')
                print(f'Con un valor total de {suma*costo[0]}')
                break