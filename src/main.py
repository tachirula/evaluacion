# hashlib lo usaremos para hashear en sha256 las claves
# evitando que en alguna database leak se muestre informacion sensible
# es decir: Que no se muestren claves en texto plano

import hashlib 

# Una clave con una longitud de 10 
# con al menos un caracter especial
# hace que un ataque de fuerza bruta sea ineficiente 
# puesto que tomaria cientos de años descifrar la clave por algoritmos matematicos avanzados

import getpass

# getpass hace que no se pueda ver la contraseña que se escribe
# importante para mayor seguridad del sistema 

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
        # el while true con try except intenta varias veces el input hasta que es valido
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
    # el while true con try except intenta varias veces el input hasta que es valido
    while True:
        try:
            op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")

    datos = clientes.get(op, False)
    if (not datos) or datos == False:
        print("no hay nada que mostrar")
        return
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
    # el while true con try except intenta varias veces el input hasta que es valido    
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
    # el while true con try except intenta varias veces el input hasta que es valido
    while True:
        try:
            mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")

    # riesgo: no se le asigno un valor por defecto a get, tampoco valida si realmente existe
    # datos = clientes.get(mod)
    # vemos si realmente existe algo
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

    # riesgo en todos los inputs: no se usa strip, por lo cual, se acepta espacios entre caracteres
    # evitamos strip en nombre como apellidos puesto que si en algun momento el proyecto escala
    # estos datos estaran en una base de datos y aqui si podemos permitir espacios en nombre 
    # como tambien apellidos, esto para mejorar legibilidad en la supuesta base de datos
    # para los demas datos, ES necesario que NO se autorice el uso de espacios

    username = input( "INGRESE NOMBRE DE USUARIO:  ").strip()

    # riesgo: la clave no se verifica, tampoco si la clave es fuerte
    # clave = input( "INGRESE PASSWORD         : ")

    clave = getpass.getpass( "INGRESE PASSWORD:  ").strip()
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
    
    nombre = input(   "INGRESE NOMBRE           : ")
    apellidos = input("INGRESE APELLIDOS        : ")
    # Riesgo: No se verifica el input de correo
    # correo = input(   "INGRESE CORREO           : ").strip() 

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

    # si pasa todas las pruebas recien se inserta los datos
    print("=======================================")
    global idusuario
    idusuario += 1
    codigo = idusuario

    # guardamos la clave hasheada
    # si en la supuesta base de datos se muestran las claves
    # estaran todas hasheadas evitando que roben cuentas

    clave_hasheada = (hashlib.sha256(clave.encode('utf-8'))).hexdigest()
    usuario = [codigo,username,clave_hasheada,nombre,apellidos,correo]
    usuarios[username] = usuario


while True:
    menuUsuarios()
    # opUsu = int(input("INGRESE OPCIÓN: "))
    # el while true con try except intenta varias veces el input hasta que es valido
    while True:
        try:
            opUsu = int(input("INGRESE OPCIÓN: "))
            break
        except ValueError:
            print("Hubo un problema al procesar su solicitud\nintente de nuevo")

    if opUsu == 1:
        user = input("Ingrese nombre de usuario: ")
        clave = getpass.getpass("Ingrese password: ")
        clave_hasheada = (hashlib.sha256(clave.encode('utf-8'))).hexdigest()
        clave_hasheada_visible = clave_hasheada[:10]
        # Se refactorizo el bloque de codigo completo para que sea mas legible
        # Se agrego continue para saltar bucles
        # Tambien la verificacion de errores se pone primero 
        # Esto para evitar bloques gigantes indentados

        conseguir_user = usuarios.get(user, False)
        if conseguir_user == False:
            input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
            continue
        if conseguir_user[2] != clave_hasheada:
            input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
            continue
        print(f"Bienvenido {conseguir_user[3]} {conseguir_user[4]} - {clave_hasheada_visible+'...'} - id: {conseguir_user[0]}.")
        input("Presiona ENTRAR para ingresar al Menú Principal.")
        while True:  # Bucle para el Menú Principal
            menuprincipal()
            #op = int(input("INGRESE OPCIÓN: "))
            # el while true con try except intenta varias veces el input hasta que es valido
            while True:
                try:
                    op = int(input("INGRESE OPCIÓN: "))
                    break
                except ValueError:
                    print("Hubo un problema al procesar su solicitud\nintente de nuevo")

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
                continue
    elif opUsu == 2:
        ingresoUsuarios()
    elif opUsu == 3:
        opSalir = input("¿DESEA SALIR [SI/NO]: ")
        if opSalir.lower() == "si":
            break
    else:
        print("Opción Fuera de Rango")
