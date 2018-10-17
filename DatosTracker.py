def separarDatos(path):
    #Retorna una lista de listas con los valores numericos extraidos de Tracker
    #Primero seleccionar en Tracker los datos COMPLETOS
    #parh: direccion del .txt donde estan los datos

    f = open(path,'r')
    datos = f.readlines()
    datos = datos[2:]
    todo = []
    for i in range(len(datos)):
        todo.append(datos[i].split('&'))

    for linea in todo:
        for i in range(len(linea)):
            if linea[i] == linea[-1]:
                linea[i] = float(linea[i].replace('\n',''))
            else:
                linea[i] = float(linea[i])
    f.close()
    return todo

