from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products

"""
Login
credenciales:

usuario:
    Luis
contrase;a:
    Luis18
"""

total_productos = len(lifestore_products) 

# Crear listas para contar las busquedas y scores.
contador_busquedas = []
contador_reseñas = []
for n in range(total_productos):
    contador_busquedas.append([n+1,0,lifestore_products[n][1]])
    contador_reseñas.append([n+1,0,0,lifestore_products[n][1]])
    for busqueda in lifestore_searches:
        if busqueda[1] == contador_busquedas[n][0]:
            contador_busquedas[n][1] += 1
    for busqueda in lifestore_sales:
        if busqueda[1] == contador_reseñas[n][0]:
            contador_reseñas[n][1] += busqueda[2]
            contador_reseñas[n][2] += 1
#Se separan los productos de los que sí tienen busquedas de los que no.
sin_busquedas = []
con_busquedas = []
con_busquedas_copy =[]
for cuenta  in contador_busquedas:
    if cuenta [1] != 0:
        con_busquedas.append(cuenta)
        con_busquedas_copy.append(cuenta)
    else:
        sin_busquedas.append(cuenta)
ord_busqueda_less = []
ord_busqueda_more = []
#Se ordenaan los valores de menor busqueeda a mayor busqueda
while con_busquedas:
    minimo = con_busquedas[0][1]
    busquedaes_actual = con_busquedas[0]
    for busqueda in con_busquedas:
        if busqueda[1] < minimo:
            minimo = busqueda[1]
            busquedaes_actual = busqueda
    ord_busqueda_less.append(busquedaes_actual)
    con_busquedas.remove(busquedaes_actual)
#Se ordenan los valoores de mayor busqueda a menoor
while con_busquedas_copy:
    maximo = con_busquedas_copy[0][1]
    busquedaes_actual = con_busquedas_copy[0]
    for busqueda in con_busquedas_copy:
        if busqueda[1] > maximo:
            maximo = busqueda[1]
            busquedaes_actual = busqueda
    ord_busqueda_more.append(busquedaes_actual)
    con_busquedas_copy.remove(busquedaes_actual)
vendidos = []
vendidos_copy = []
promedio = []
promedio_copy = []
sin_registro = []
for score in contador_reseñas:
    if score[2] != 0:
        vendidos.append([score[0],score[2],score[3]])
        vendidos_copy.append([score[0],score[2],score[3]])
        promedio.append([score[0], round(score[1]/score[2],2),score[3]])
        promedio_copy.append([score[0], round(score[1]/score[2],2),score[3]])
    else:
        sin_registro.append([score[0], "Sin registro de venta"])
#Se ordenan productos mas vendidos, reseña de mayyoor a menor y al réves
mas_vendidos = []
menos_vendidos = []
promedio_mas = []
promedio_menos = []
while vendidos:
    minimo = vendidos[0][1]
    ventas_actual = vendidos[0]
    for ventas in vendidos:
        if ventas[1] < minimo:
            minimo = ventas[1]
            ventas_actual = ventas
    menos_vendidos.append(ventas_actual)
    vendidos.remove(ventas_actual)
while promedio_copy:
    maximo =promedio_copy[0][1]
    promedio_actual = promedio_copy[0]
    for puntuacion in promedio_copy:
        if puntuacion[1] > maximo:
            maximo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_mas.append(promedio_actual)
    promedio_copy.remove(promedio_actual)
while promedio:
    minimo = promedio[0][1]
    promedio_actual = promedio[0]
    for puntuacion in promedio:
        if puntuacion[1] < minimo:
            minimo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_menos.append(promedio_actual)
    promedio.remove(promedio_actual)
while vendidos_copy:
    maximo = vendidos_copy[0][1]
    vendidos_actual = vendidos_copy[0]
    for ventas in vendidos_copy:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    mas_vendidos.append(vendidos_actual)
    vendidos_copy.remove(vendidos_actual)
#Se crean listas para el calculo de ventas por mes y anual, tambien se ordenan de mayor a menor
por_dia = []
for sale in lifestore_sales:
    por_dia.append([lifestore_products[sale[1]-1][2],sale[3][3:],sale[4]])
lista_mes = []
lista_año= []
for mes in por_dia:
    if not mes[1] in lista_mes:
        lista_mes.append(mes[1])
    if not mes[1][-4:] in lista_año:
        lista_año.append(mes[1][-4:])
contador_ventas_mensual = []
for mes in lista_mes:
    contador_ventas_mensual.append([mes, 0])
for sale in por_dia:
    for mes in contador_ventas_mensual:
        if sale[1] == mes[0]:
            mes[1] += sale[0]
contador_ventas_anual = []
for año in lista_año:
    contador_ventas_anual.append([año,0,0])
for sale in contador_ventas_mensual:
    for año in contador_ventas_anual:
        if sale[0][-4:] == año[0]:
            año[1] += sale[1]
            año[2] += 1
meses_mayor_ventas = []
while contador_ventas_mensual:
    maximo = contador_ventas_mensual[0][1]
    vendidos_actual = contador_ventas_mensual[0]
    for ventas in contador_ventas_mensual:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    meses_mayor_ventas.append(vendidos_actual)
    contador_ventas_mensual.remove(vendidos_actual)
meses = ["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]

# Pantalla de inicio lifestore.
print("¡Bienvenido al sitio de análisis de ventas de Lifestore!")

"""
Login
credenciales:

usuario:
    Luis
contrase;a:
    Luis18
"""

usuarioAccedio = False
intentos = 0

# Bienvenida!
advertencia = input("""Advertencía!!!!. Solo las personas de gerencía con datos de registro podran ingresar.
¿Cuentas con los datos de acceso? (si/no)
""") == "si"
mensaje_bienvenida = "Bienvenide al sistema!\nAccede con tus credenciales"
print(mensaje_bienvenida)

# Recibo constantemente sus intentos
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input("Usuario: ")
    contras = input("Contraseña: ")
    intentos += 1
    # Reviso si el par coincide
    if usuario == "Luis" and contras == "Luis18":
        usuarioAccedio = True
        print("Hola de nuevo " + (usuario) + "!")
    else:
        # print('Tienes', 3 - intentos, 'intentos restantes')
        print(f"Tienes {3 - intentos} intentos restantes")
        if usuario == "Luis":
            print('Te equivocaste en la contraseña')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<< INGRESO EXITOSO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print("<<<<< " + usuario + ", bienvenido al Menú del sistema de reporte de ventas de LifeStore >>>>>")

if usuario == "Luis" and contras == "Luis18":
    administrador = 1

opcion = 0
if administrador == 1:
    while opcion != 4:
        print("""
            1: Lista de ventas de productos
            2: Lista de reseñas de productos
            3: Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año
            4: Salir
            """)
        opcion = input((usuario) + ", ingresa una opción para consultar en el reporte de ventas: ")

        eleccion = 0
        if opcion.isnumeric():
            if opcion == "1": # Ingresa al submenu Listoa ventas de productos.
                while eleccion != "3":
                    print("<<<<< " + (usuario) + """, bienvenido al Menú  del reporte de ventas >>>>>
                    [1] Lista de los productos más vendidos y más buscados.
                    [2] Lista de los productos menos vendidos y menos buscados.
                    [3] Regresar
                    """)
                    eleccion = input("Ingresa una opción: ")
                    if eleccion == "1": # Se consulta la info de la lista de los 5 Iproductos más vendidos y más buscados.
                    # Productos más vendidos
                        print("{} más vendidos:".format(10))
                        for n in range(5):
                            print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(mas_vendidos[n][1]),mas_vendidos[n][2].split(",")[0]))
                    # Productos más buscados
                        print("{} más buscados:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(ord_busqueda_more[n][1]),ord_busqueda_more[n][2].split(",")[0]))
                    elif eleccion == "2": #Se consulta la info de la lista de los 5 Iproductos menos vendidos y menos buscados.
                    # Productos menos vendidos
                        print("{} menos vendidos:".format(5))
                        for n in range(5):
                            print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(menos_vendidos[n][1]),menos_vendidos[n][2].split(",")[0]))
                    # Productos menos buscados
                        print("{} menos buscados:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(ord_busqueda_less[n][1]),ord_busqueda_less[n][2].split(",")[0]))
                    elif eleccion == "3": # Con este se regresa al menu antetrior.
                        continue
                    else:
                        print("Ingrese una opción valida")
            elif opcion == "2":
                #Productos con mejores reseñas
                print("{} Mejores reseñas:".format(20))
                for n in range(5):
                    print("{:>2s}. Calificación {:>2s}/5 de {}".format(str(n+1),str(promedio_mas[n][1]),promedio_mas[n][2].split(",")[0]))
                    
                # Productos con peores reseñas
                print("{} Peores reseñas:".format(5))
                for n in range(5):
                    print("{:>2s}. Calificación {:>2s}/5  de {}".format(str(n+1),str(promedio_menos[n][1]),promedio_menos[n][2].split(",")[0]))
                    
                  
            elif opcion == "3":
                #Ventas anaules y mensuales, promedio de ventas anuales y mensuales
                print("Ventas Anuales")
                for año in contador_ventas_anual:
                    print("{}: $ {},{}.00".format(año[0],str(año[1])[:-3],str(año[1])[-3:]))
                print("Promedio mensual")
                for año in contador_ventas_anual:
                    promedio_mensual = str(round(año[1]/año[2],2))
                    print("{}: $ {}".format(año[0],promedio_mensual))
                print("Ventas por mes")
                indice = 0
                for mes in meses_mayor_ventas:
                    indice += 1
                    a = int(mes[0][:2])-1
                    print("{:>2s}. {:>10s} {}: ${},{}.00".format(str(indice),meses[a],mes[0][-4:],str(mes[1])[:-3],str(mes[1])[-3:]))
                    
            elif opcion == "4": #Con esta te sales del menu y cierra programa.
                print("Sesion terminada. "+ (usuario) + " nos vemos. Esperamos su feedback para poder mejorar el reporte en futuras ocasiones")
                break

            else:
                print("Opción no valida.")


