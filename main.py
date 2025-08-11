

fin_menu = True

while fin_menu:

   try:
       print("\t\t\tBienvenido usuario: ")
       print("1. Opcion 1 \n2. Opcion 2 \n3. Opcion 3 \n4.Opcion 4 5. Salir")
       op = int(input('Seleccione una opción: '))
       match op:
           case 1:
               print('Opcion 1')
           case 2:
               print('Opcion 2')
           case 3:
               print('Opcion 3')
           case 4:
               print('Opcion 4')
           case 5:
               while True:
                   conf = input('¿Esta seguro que desea salir? S/N')
                   if conf.upper() == "S":
                       print('Adios')
                       op = False
                       break
                   elif conf.upper() == "N":
                       break
                   else:
                       print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')

           case _:
            print('Valor incorrecto - ¡Por favor verifique su respuesta!')

   except ValueError as e:
       print('Ocurrio un error favor de volver a intentarlo')
