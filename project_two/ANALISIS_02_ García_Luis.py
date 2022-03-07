import csv
import pandas as pd


print("Bienvenido a Synergy Logistics")
print("Secciones:\n 1)Exportaciones\n 2)Importaciones\n cada opcion muestra: \n a)Mejores Rutas,b)Transportes mas usados, c)Mayor valor \n" )

continuar = input("Continuar:(si/no)")
while continuar == "si":
    print("Secciones:\n 1)Exportaciones\n 2)Importaciones")
    seleccionar =input("Selecciona una opción: ")
    
    opcion_1 = False
    opcion_1 = False
    if seleccionar == "1":
        print("Seleccionaste Exportaciones\n Cargando...")
        opcion_1 = True
    elif seleccionar == "2":
        print("Seleccionaste Importaciones\n Cargando...")
        opcion_2 = True
    else:
        print(("Error, algo salio mal...."))
        print(("Intenta 1 ,2"))
        break

    file = []
    
    with open ("synergy_logistics_database.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        
        for columns in reader:
            file.append(columns)
    #RUTAS MAS DEMANDADAS EN EXPORTACIONES       
    def routes(direction):
    
        count = 0  
        count_exp = []
        exports = []  
        for route in file:
            if route[1] == direction:
                route_exp = [route[2],route[3]]
                #trans_exp.append([route[7],int(route[9])])
            #    print(route_exp)
                
            
                if route_exp not in exports:
                    for exp in file:
                        if route_exp == [exp[2],exp[3]]:
                            count += 1
                    exports.append(route_exp)
                    count_exp.append([route[2],route[3],count])
                    count = 0 
                
                    
        count_exp.sort(reverse = True, key = lambda x:x[2])
        df =pd.DataFrame(count_exp[:10], columns =["Origen","Destino","Total"])
        #df.to_csv("top10_imp.csv", index = False)
        return (print(df))
    #routes("Exports")
    #TRANSPORTES EN EXPORTACIONES MAS IMPORTANTES DE ACUERDO AL VALOR
    def transports(direction):
        trans_exp = []
        for route in file:
            if route[1] == direction:
                trans_exp.append([route[7],int(route[9])])
        sea_value = []
        air_value = []
        rail_value = []
        road_value = []
        for transport in trans_exp:
            if transport[0] == "Sea":
                sea_value.append(transport[1])
                total_sea = sum(sea_value)      
            elif transport[0] == "Air":
                air_value.append(transport[1])
                total_air = sum(air_value)
            elif transport[0] == "Rail":
                rail_value.append(transport[1])
                total_rail = sum(rail_value)
        
            elif transport[0] == "Road":
                road_value.append(transport[1])
                total_road = sum(road_value)
        
            else:
                "Transporte no disponible"
        exp_transport = [["Air",total_air],["Rail",total_rail],["Road",total_road],["Sea",total_sea]]
        
        exp_transport.sort(reverse = True, key = lambda x:x[1])
        df_transport =pd.DataFrame(exp_transport[:3], columns = ["Transporte","Total"])
        #df_transport.to_csv("tranporte_imp.csv", index = False)
        return(print(df_transport))
    
    #transports("Imports")
    paises = []
    origin_value =[]
    paises_exp =[]
    pais_value= []
    pais_value2 = []
    paises_imp = []
    paises2 = []
    dest_value = []
    for route in file:
        
        if route[1] == "Exports":
            pais_value.append(int(route[9]))
            paises_exp.append(route[2])
            for pais in paises_exp:
                if pais not in paises:
                    paises.append(route[2])
        elif route[1] == "Imports":
            pais_value2.append(int(route[9]))
            paises_imp.append(route[3])
            for pais in paises_imp:
                if pais not in paises2:
                    paises2.append(route[3])
              
    total = sum(pais_value)
    total2 = sum(pais_value2)
    #print(total)
    #Mayores exportaciones por pais
    for count_pais in range(len(paises)):
        count = 0
        suma = 0
        for pais_exp in range(len(paises_exp)): 
            if paises_exp[pais_exp] == paises[count_pais]: 
                count = count + 1
                suma = suma + pais_value[pais_exp]
        origin_value.append([paises[count_pais],count, suma,((suma*100)/total)])
    
    origin_value.sort(reverse = True, key = lambda x:x[2])
    df_total =pd.DataFrame(origin_value[:7], columns = ["Pais Exportador","Cantidad"," Valor","Porcentaje"])
    #df_total.to_csv("total_exp.csv", index = False)
    #print(df_total) 
    #print(pais_value)
    #print(origin_value)
    
    #Mayores Importaciones por pais
    for count_pais2 in range(len(paises2)):
        count2 = 0
        suma2 = 0
        for pais_imp in range(len(paises_imp)): 
            if paises_imp[pais_imp] == paises2[count_pais2]: 
                count2 = count2 + 1
                suma2 = suma2 + pais_value2[pais_imp]
        dest_value.append([paises2[count_pais2],count2, suma2,((suma2*100)/total2)])
    
    dest_value.sort(reverse = True, key = lambda x:x[2])
    df_total2 =pd.DataFrame(dest_value[:7], columns = ["Pais Importador","Cantidad"," Valor","Porcentaje"])
    #df_total2.to_csv("total_imp.csv", index = False)
    #print(df_total2)
    
    if opcion_1 == 1:
        print("\n Las mejores rutas son:\n")
        rutas = routes("Exports")
        print("\n Los transportes mas usados son:\n")
        transporte = transports("Exports")
        print("\n Los paises que generan mayor valor(80%) son:\n")
        print(df_total)
        continuar = input("Ir de nuevo al menu de opciones (si/no): ")
        
    elif opcion_2 == 1:
        print("\n Las mejores rutas son:\n")
        rutas = routes("Imports")
        print("\n Los transportes mas usados son:\n")
        transporte = transports("Imports")
        print("\n Los paises que generan mayor valor(80%) son:\n")
        print(df_total2)
        continuar = input("Ir de nuevo al menu de opciones (si/no): ")
        
        if continuar == "si":
            print("cargando...")
        elif continuar == "no":
            print("Cerrando programa..")
        else: print("intenta unicamente: si / no")
        continue    

else:
    print("Desconectando... elegiste:[no] o cometiste un error\n"
          "Ingresa de nuevo")