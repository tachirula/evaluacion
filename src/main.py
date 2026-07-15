
MINIMO_LONGITUD_CLAVE = 10
CHAR_ESPECIALES = '!#$%&()*+,-.:;<=>?@[]^_`{|}~'

clientes = {}
usuarios = {}
idcliente = 0
idusuario = 0

def menuprincipal():
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.- (E) Salir            ")
    print("================================")

def menumostrar():
    print("================================")
    print("     M E N Ú  M O S T R A R     ")
    print("================================")
    print("       1.- MOSTRAR TODO         ")
    print("       2.- MOSTRAR UNO          ")
    print("       3.- MOSTRAR PARCIAL      ")
    print("       4.- VOLVER               ")
    print("================================")

def ingresardatos():
    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")
    run = input("INGRESE RUN : ")
    nombre=input("INGRESE NOMBRE : ")
    apellido=input("INGRESE APELLIDO : ")
    direccion=input("INGRESE DIRECCION : ")
    fono=input("INGRESE TELEFONO : ")
    correo=input("INGRESE CORREO : ")
    tipos = [
        [101,"Plata"],[102,"Oro"],[103,"Platino"]
    ]
    print("--------------------------------------------")
    for tipo in tipos:
        print(
            " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
    print("--------------------------------------------")
    tipo = input("Ingrese el codigo del Tipo de Cliente: ")
    monto=input("INGRESE MONTO CREDITO : ")
    global idcliente    
    idcliente += 1
    codigo = idcliente
    deuda = 0
    cliente = [codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda]
    clientes[idcliente]=cliente

def mostrar():
    while(True):
        menumostrar()

        # riesgo: transformar un str a entero sin comprobaciones
        # op2 = int(input("  INGRESE OPCIÓN : "))

        while True:
            try:
                op2 = int(input("  INGRESE OPCIÓN : "))
                break
            except ValueError:
                print("Hubo un problema al procesar su solicitud\nintente de nuevo")

        if op2 == 1:
            mostrartodo()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        elif op2 == 2:
            mostraruno()
        elif op2 == 3:
            mostrarparcial()
        if op2 == 4:
            break
        else:
            print("Opción Fuera de Rango")

def mostrartodo():
    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")
    for cliente,dato in clientes.items():
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():
    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")

    # riesgo: transformar un str a entero sin comprobaciones
    # op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))

    while True:
        try:
            op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")

    datos = clientes.get(op)
    print(datos)
    print("\n=======================================")
    print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
    print("=======================================")
    print(" ID            : {} ".format(datos[0]))
    print(" RUN           : {} ".format(datos[1]))
    print(" NOMBRE        : {} ".format(datos[2]))
    print(" APELLIDO      : {} ".format(datos[3]))
    print(" DIRECCION     : {} ".format(datos[4]))
    print(" FONO          : {} ".format(datos[5]))
    print(" CORREO        : {} ".format(datos[6]))
    print(" TIPO          : {} ".format(datos[9]))
    print(" MONTO CREDITO : {} ".format(datos[7]))
    print(" DEUDA         : {} ".format(datos[8]))
    print("-----------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def mostrarparcial():
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")

    # riesgo: transformar un str a entero sin comprobaciones
    # cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))

    while True:
        try:
            cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")
    
    datos = list(clientes.items())[:cant]
    for cliente,dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[9], dato[7], dato[8]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def modificardatos():
    listanuevos=[]
    print("===================================")
    print("      MODULO MODIFICAR CLIENTE     ")
    print("===================================")
    mostrartodo()

    # riesgo: transformar un str a entero sin comprobaciones
    # mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
    while True:
        try:
            mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")

    # riesgo: no se le asigno un valor por defecto a get, tampoco valida si realmente existe
    # datos = clientes.get(mod)
    datos = clientes.get(mod, False)
    if datos == False:
        print("No se encontro el modulo a modificar.")
        return
    
    print(" ID         : {} ".format(datos[0]))
    listanuevos.append(datos[0])
    print(" RUN        : {} ".format(datos[1]))
    listanuevos.append(datos[1])

    opm=input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
        nombrenuevo=input("INGRESE NOMBRE : ")
        listanuevos.append(nombrenuevo)
    else:
        listanuevos.append(datos[2])
    opm = input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3]))
    if opm.lower() == "si":
        apellidonuevo= input("INGRESE APELLIDO : ")
        listanuevos.append(apellidonuevo)
    else:
        listanuevos.append(datos[3])
    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4]))
    if opm.lower() == "si":
        direcnueva = input("INGRESE DIRECCION : ")
        listanuevos.append(direcnueva)
    else:
        listanuevos.append(datos[4])
    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5]))
    if opm.lower() == "si":
        fononuevo= input("INGRESE TELEFONO : ")
        listanuevos.append(fononuevo)
    else:
        listanuevos.append(datos[5])
    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6]))
    if opm.lower() == "si":
        correonuevo = input("INGRESE EL CORREO : ")
        listanuevos.append(correonuevo)
    else:
        listanuevos.append(datos[6])
    opm = input("DESEA MODIFICAR LA DEUDA : {} - [SI/NO] ".format(datos[9]))
    if opm.lower() == "si":
        deudanuevo= input("INGRESE DEUDA : ")
        listanuevos.append(deudanuevo)
    else:
        listanuevos.append(datos[9])
    opm = input("DESEA MODIFICAR EL MONTO DE CREDITO : {} - [SI/NO] ".format(datos[8]))
    if opm.lower() == "si":
        montonuevo= input("INGRESE MONTO DE CREDITO : ")
        listanuevos.append(montonuevo)
    else:
        listanuevos.append(datos[8])
    opm = input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
        tipos = [
            [101,"Plata"],[102,"Oro"],[103,"Platino"]
        ]
        print("--------------------------------------------")
        for tipo in tipos:
            print(
                " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
        print("--------------------------------------------")
        
        tiponuevo = input("INGRESE EL TIPO : ")
        listanuevos.append(tiponuevo)
    else:
        listanuevos.append(datos[7])
    
    clientes[mod]=listanuevos


def eliminardatos():
    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")
    mostrartodo()
    elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    del clientes[elim]

# --------------------------------------

def menuUsuarios():
    print("================================")
    print("   M E N Ú  U S U A R I O S     ")
    print("================================")
    print("       1.-  INICIAR SESIÓN      ")
    print("       2.-  REGISTRAR USUARIO   ")
    print("       3.-  Salir               ")
    print("================================")

def ingresoUsuarios():
    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")

    # riesgo en todos los inputs: no se usa strip por lo cual se acepta espacios entre caracteres

    username = input( "INGRESE NOMBRE DE USUARIO:  ").strip()

    # riesgo: la clave no puede contener espacios, tampoco se verifica si la clave es fuerte
    # clave = input( "INGRESE PASSWORD         : ")

    clave = input( "INGRESE PASSWORD:  ").strip()
    if len(clave) < MINIMO_LONGITUD_CLAVE:
        print(f"su clave debe contar con una longitud de {MINIMO_LONGITUD_CLAVE} como minimo")
        return
    flag = False
    for char in clave:
        if char in CHAR_ESPECIALES:
            flag = True
            break
    if flag == False:
        print("su clave debe contener minimo 1 caracter especial")
        return
    
    nombre = input(   "INGRESE NOMBRE           : ") # El usuario puede tener mas de un nombre
    apellidos = input("INGRESE APELLIDOS        : ") # APELLIDOS en plural, pide todos, no se usa strip.
    # Riesgo: No se verifica el input de correo
    #correo = input(   "INGRESE CORREO           : ").strip() 

    correo = input(   "INGRESE CORREO:  ").strip() 
    empezar_contado = False
    dominio = []
    usuario = []
    for buscar_dom in correo:
        if buscar_dom == '@':
            empezar_contado = True
        elif empezar_contado == True:
            dominio.append(buscar_dom)
    
    for buscar_usuario in correo:
        if not buscar_usuario == '@':
            usuario.append(buscar_usuario)
        else:
            break

    if (not '.' in dominio) or (not usuario):
        print("correo invalido")


    print("=======================================")
    global idusuario
    idusuario += 1
    codigo = idusuario
    usuario = [codigo,username,clave,nombre,apellidos,correo]
    usuarios[username] = usuario


while True:
    menuUsuarios()
    opUsu = int(input("INGRESE OPCIÓN: "))

    if opUsu == 1:
        user = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese password: ")
        if usuarios.get(user):
            usuario = usuarios.get(user)
            if usuario[2] == clave:
                print(f"Bienvenido {usuario[3]} {usuario[4]} - {usuario[2]} - id: {usuario[0]}.")
                input("Presiona ENTRAR para ingresar al Menú Principal.")
                while True:  # Bucle para el Menú Principal
                    menuprincipal()
                    op = int(input("INGRESE OPCIÓN: "))
                    if op == 1:
                        ingresardatos()
                    elif op == 2:
                        mostrar()
                    elif op == 3:
                        modificardatos()
                    elif op == 4:
                        eliminardatos()
                    elif op == 5:
                        opSalir = input("¿DESEA SALIR [SI/NO]: ")
                        if opSalir.lower() == "si":
                            break  # Salir del bucle del Menú Principal
                    else:
                        print("Opción Fuera de Rango")
                break  # Salir del bucle del Menú de Usuarios
            else:
                input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
        else:
            input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
    elif opUsu == 2:
        ingresoUsuarios()
    elif opUsu == 3:
        opSalir = input("¿DESEA SALIR [SI/NO]: ")
        if opSalir.lower() == "si":
            break
    else:
        print("Opción Fuera de Rango")
