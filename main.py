

fin_menu = True

while fin_menu:

   try:
       print("\t\t\tBienvenido usuario: ")
       print("1. Ingreso de nombre \n2. Ingreso de numero entero \n3. Ingreso de contraseña \n4. Salir")
       op = int(input('Seleccione una opción: '))
       match op:
           case 1:
               print('Pureba de ingreso de nombre: ')
               while True:
                   nombre = input('Ingrese sus nombres').strip()
                   if nombre !="":
                       print(f'Bienvenido {nombre}')
                       break
                   else:
                       print('Error - Debe ingresar al menos un nombre')
                       p1 = input('¿Desea volver a intentarlo? S/N')
                       if p1.upper() == "S":
                           print('Por favor ingrese un nombre valido')
                       elif p1.upper()== "N":
                           print('Regresando al menu principal')
                           break
                       else:
                           print('Error-Ingrese un valor valido S o N')

           case 2:
               print('Prueba el ingreso de un numero entero: ')
               while True:
                   try:
                       numero = int(input('Ingrese un numero entero: '))
                       print(f'numero ingresado {numero}')
                       break

                   except ValueError as e:
                       print('Ocurrio un error de casteo por favor volver a intentarlo')


           case 3:
               print('Ingreso de contraseña: \nSolo tienes 3 intentos\n')
               contra = "Erick1234"
               cont =0
               while cont<3:
                   ingreso = input('Ingrese la contraseña: ')
                   if ingreso == contra:
                       print('Bienvenido Erick!!!!')
                       break
                   elif ingreso!= contra:
                       cont +=1
                       print(f'Ingreso invalido por favor vuelva a intentarlo le quedan {3 - cont}')

           case 4:
               while True:
                   conf = input('¿Esta seguro que desea salir? S/N')
                   if conf.upper() == "S":
                       print('Adios')
                       fin_menu = False
                       break
                   elif conf.upper() == "N":
                       break
                   else:
                       print(f'La opcion {conf} no existe vuelve a intentarlo con S para si o N para no')

           case _:
            print('Valor incorrecto - ¡Por favor verifique su respuesta!')

   except ValueError as e:
       print('Ocurrio un error favor de volver a intentarlo')
