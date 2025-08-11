

fin_menu = True

while fin_menu:

   try:
       print("\t\t\tBienvenido usuario: ")
       print("1. Opcion 1 \n2. Opcion 2 \n3. Opcion 3 \n4.Opcion 4 5. Salir")
       op = int(input('Seleccione una opción: '))
       match op:
           case 1:
           case 2:
           case 3:
           case 4:
           case 5:
            print('¿Esta seguro que desea salir?')

           case _:
            print('Valor incorrecto - ¡Por favor verifique su respuesta!')

   except ValueError as e:
       print('Ocurrio un error favor de volver a intentarlo')
