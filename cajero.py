'''Hacer uan jejercicio que simule  un cajero automatico 
con las siguientes opciones:
1.Ingresar dinero
2.Retirar dinero
3.Mostrar saldo disponible
4.Salir'''

saldo=1000
print('\t MENU')
print('1.Hacer depocito...')
print('2.Retirar dinero de la cuenta...')
print('3.Mostrar saldo disponible...')
print('4.Salir...')
opcion= int(input('Digite una opcion de menu:'))

if opcion==1:
    depocito=float(input('Cantidad a ingresar: $'))
    saldo += depocito
    print(f'Tu nuevo saldo es de: {saldo}')
elif opcion==2:
    retirar=float(input('Cuanrto dinero decea retirar: $'))
    if retirar<=saldo:
        saldo-=retirar
        print(f'Tu nuevo saldo es: ${saldo}')
    else:
        print('No cuetas con saldo suficiente en tu cuenta')
elif opcion==3:
    print(f'Tu saldo es de ${saldo}')
elif opcion==4:
    print('GRacias por su preferencia')
else:
    print('Seleccione una opcion de menu:')
    