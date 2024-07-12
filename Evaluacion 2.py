#Evaluacion 2 
ciclo = True
paciente1=[]
paciente2=[]
while ciclo:
    usuario = input('Ingresa un usuario: ').lower()
    if usuario == 'jaravena':
        psswd=input('Ingrese su contraseña: ')
        if psswd =='clave03':
            if len(paciente1)>0:
                op2=int(input('(1)Consultar cuenta\n(2)Pagar cuenta\n'))
                if op2==1:
                    print(paciente1)
                elif op2==2:
                    print(f'total es: ${total}')     
            else:
              print('Esta vacía la cuenta:C ')
        else:
             print('Contraseña incorrecta...')     

        salir=int(input('(1)Continuar\n(2)Salir\n'))
        if salir==2:
             ciclo=False

    elif usuario == 'maravena':
        psswd=input('Ingrese su contraseña: ')
        if psswd =='clave02':
            if len(paciente2)>0:
                op2=int(input('(1)Consultar cuenta\n(2)Pagar cuenta\n'))
                if op2==1:
                    print(paciente2)
                elif op2==2:
                    print(f'total es: ${total}')     
            else:
                print('Esta vacía la cuenta:C ')
        else:
             print('Contraseña incorrecta...')   
        salir=int(input('(1)Continuar\n(2)Salir\n'))
        if salir==2:
             ciclo=False

    elif  usuario == 'chernandez':
        psswd=input('Ingrese su contraseña: ')    
        if psswd =='clave01':
            op=int(input("a qué cuenta desea ingresar\n(1)Juan Aravena\n(2)Martin Aravena\n"))
            count=int(input('Ingrese cantidad de cuentas: '))
            for i in range (count):
                if op == 1:
                    tipoprestacion=input('Ingrese tipo de prestación: ').lower()
                    paciente1.append(tipoprestacion)
                    denoprestacion=input('Ingrese denominacionde prestacion: ').lower()
                    paciente1.append(denoprestacion)
                    valorneto=float(input('Ingrese valor neto: '))
                    paciente1.append(valorneto)
                    if tipoprestacion=='farmaco':
                        cantidadpagar= valorneto*0.10
                    elif tipoprestacion=='examen':
                            cantidadpagar= valorneto*0.20
                    elif tipoprestacion=='consulta':
                            cantidadpagar= valorneto*0.80

                    total=round(cantidadpagar*1.19,1)
                    paciente1.append(total)
                    #print(f'datos de la cuenta:\n{paciente1}\ncantidad a pagar: ${total}')
                    cantidadpagar=0
                if op==2:
                    tipoprestacion=input('Ingrese tipo de prestación: ').lower()
                    paciente2.append(tipoprestacion)
                    denoprestacion=input('Ingrese denominacionde prestacion: ').lower()
                    paciente2.append(denoprestacion)
                    valorneto=float(input('Ingrese valor neto: '))
                    paciente2.append(valorneto)
                    if tipoprestacion=='farmaco':
                        cantidadpagar= valorneto*0.10
                    elif tipoprestacion=='examen':
                            cantidadpagar= valorneto*0.20
                    elif tipoprestacion=='consulta':
                            cantidadpagar= valorneto*0.80

                    total=round(cantidadpagar*1.19,1)
                    paciente2.append(total)
                    #print(f'datos de la cuenta:\n{paciente2}\ncantidad a pagar: ${total}')
                    cantidadpagar=0
        else:
             print('Contraseña incorrecta...')               

        salir=int(input('(1)Continuar\n(2)Salir\n'))
        if salir==2:
             ciclo=False     