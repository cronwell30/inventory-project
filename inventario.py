products={}
flag=True

while True:
  print('''
    1. Añadir productos.
    2. Buscar producto.
    3. Inventario.
    4. Ver productos.''')
  
  respuesta=int(input('Ingrese su opcion: '))
  
  if respuesta == 1:
    print('\t Agregar producto nuevo')
    name=str(input('Nombre de el producto: '))
    code=int(input('Codigo de producto: '))
    quantity=int(input('Cantidad de producto: '))
    coste=float(input('Precio de venta :$'))
    products [name]=code,quantity,coste
    print(products)
  elif respuesta == 2:
    search=str(input('Nombre del producto a buscar: '))
    if search in products:
      print(f'Detalles de producto {products[search]}')
  elif respuesta == 3:
    search=str(input('Producto a inventariar: '))
    if search in products:
      contado=[]
      suma=0
      while contado != quantity:
        encontrado=int(input('Cantidad encontrada: '))
        contado.append(encontrado)
        print(contado)
        for i in contado:
          suma=sum(contado)
        print(suma)
        if suma>=quantity:
          terminar=str(input('A encotrado todos los productos deceas terminar (y/n): '))
          if terminar=='y':
            print(f'valor de inventario {suma*coste}')
            break
  elif respuesta == 4:
    for i in products:
      print(products[i])
  elif respuesta == 5:
    venta=(str(input('Producto a vender: ')))
    if venta in products:
      cantidad=int(input('Cabntidad a vender: '))
      menos = quantity - cantidad
      quantity.replace(menos)
      print(products)