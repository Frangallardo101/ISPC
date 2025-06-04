from datetime import datetime
list_dispositivo =[]

 # Funcion para agregar Dispositivos
def agregar(nombre_dispositivo,marca,modelo,tipo,color,temperatura,tiempo,consumo_energia,voltaje,ubicacion,estado):
    
    
    dispositivo = {"nombre_dispositivo":nombre_dispositivo,"marca":marca,"modelo":modelo,"tipo":tipo,"color":color,"temperatura":temperatura,"tiempo":tiempo, 
                   "consumo_energia": consumo_energia,"voltaje":voltaje,"ubicacion":ubicacion,"estado":estado}
    
    list_dispositivo.append(dispositivo)  
    return "\n Se agrego con exito"
    

def mostrar(): # Funcion para mostar todos los dispositivos
    
    if len(list_dispositivo)== 0:
        
        return "Sin dispositivos"
    
    lista_dispositivos = []
    
    for dispositivo in list_dispositivo:
        
        encontrado = True
        
        lista_dispositivos.append(dispositivo)
        
    return lista_dispositivos

#Funcion para buscar dispositivo p
def buscar(busqueda):
    
    encontrado = False
    
    for dispositivo in list_dispositivo:
        
        if dispositivo['nombre_dispositivo'] == busqueda:
            
            encontrado = True
            
            return(dispositivo) 
        
    if encontrado== False:
        
        return "No se encontro el dispositivo"

#Funcion para eliminar un dispositivo
def eliminar(busqueda):
    
    encontrado = False
    
    for dispositivo in list_dispositivo:
        
        if dispositivo['nombre_dispositivo'] == busqueda:
            
            encontrado = True
            
            list_dispositivo.remove(dispositivo)
            
    if encontrado == True:
        return "Se Elimino con exito"
        
    if encontrado== False:
        return "No se encontro el dispositivo"

#Funcion para Apagar luces 
def apagar_luces(busqueda):
    
    for dispositivo in list_dispositivo:
        
        if dispositivo["tipo"] == 2 and dispositivo["ubicacion"] == busqueda:
            
            dispositivo["estado"]=0
   
#Funcion para Prender Luces           
def prender_luces(busqueda):
    
    for dispositivo in list_dispositivo:
        
        if dispositivo["tipo"] == 2 and dispositivo["ubicacion"] == busqueda:
            
            dispositivo["estado"]=1
            
    return "Las luces fueron encendidas"

#Funciones para mostrar luces prendidas
def mostrar_luces_prendidos():
    
    luces_prendidas = []
    
    for dispositivo in list_dispositivo:
        
        if dispositivo["estado"] == 1 and dispositivo["tipo"]==2:
            
            luces_prendidas.append(f'Las luces de {dispositivo["ubicacion"]} estan  prendidas')
    
    return luces_prendidas

#Funciones para mostrar luces apagado
def mostrar_luces_apagado():
    
    for dispositivo in list_dispositivo:
        
        luces_apagadas = []
        
        if dispositivo["estado"] == 0 and dispositivo["tipo"]==2:
            
            luces_apagadas.append(f'Las luces de {dispositivo["ubicacion"]} estan apagadas')
    
    return luces_apagadas

#Funcion para configurar horario para prender las luces.
def luces_modo_Noche(hora_prendido,minuto_prendido,ubicacion_exterior):
    # obtenemos la hora actual del sistema
    ahora = datetime.now()
    
    hora_actual = ahora.hour 
    
    minuto_actual = ahora.minute
    
    if hora_prendido == hora_actual and minuto_actual == minuto_prendido:
        
        encendido = False # variable para verificar si se encontro alguna luz prendida
        
        for dispositivo in list_dispositivo:
            
            if dispositivo["tipo"] == 2 and dispositivo["ubicacion"] ==  ubicacion_exterior:
                                
                dispositivo["estado"] = 1  # encendemos la luz 
                
                encendido = True # indicamos que se encontro y se prendio una luz
                
                return (f'Se encendió la luz de {dispositivo["ubicacion"]} con éxito.')
             
            # Si no se encontró ningún dispositivo compatible
        if not encendido:
            
            return (f" No se encontró ningún dispositivo de iluminación en '{ubicacion_exterior}'.")
    else:
        
        return(f" No es la hora configurada aún. Hora actual: {hora_actual} minito actual {minuto_actual}, hora configurada: {hora_prendido} minuto configurado {minuto_prendido}")
                 
#Funcion para configurar horario para apagar luces para ahorro de enrgia.     
def luces_modo_ahorro(hora_apagado,minuto_apagado,ubicacion_exterior):
    # obtenemos la hora actual del sistema
    ahora = datetime.now()
    
    hora_actual = ahora.hour 
    
    minuto_actual = ahora.minute
    
    if hora_apagado == hora_actual and minuto_actual == minuto_apagado:
        
        encendido = False # variable para verificar si se encontro alguna luz prendida
        
        for dispositivo in list_dispositivo:
            
            if dispositivo["tipo"] == 2 and dispositivo["ubicacion"] ==  ubicacion_exterior:
                
                dispositivo["estado"] = 0  # encendemo la luz 
                
                encendido = True # indicamos que se encontro y se prendio una luz
                
                return (f'Se encendió la luz de {ubicacion_exterior} con éxito.')
             
            # Si no se encontró ningún dispositivo compatible
        if not encendido:
            
            return(f" No se encontró ningún dispositivo de iluminación en '{ubicacion_exterior}'.")
    else:
        
        return(f" No es la hora configurada aún. Hora actual: {hora_actual} minuto actual: {minuto_actual}, hora configurada: {hora_apagado} minuto configurado: {minuto_apagado}")
 
def calefacion_ambiente(temperatura_hoy):
    
    for dispositivo in list_dispositivo:
        
        if temperatura_hoy <=18 :
            
            for dispositivo in list_dispositivo:

                if dispositivo["tipo"]== 3 :
            
                    dispositivo["temperatura "]= 24
                    
                    return(f'Se prendio automaticamente el {dispositivo["nombre_dispositivo"]} ahora la temperatura es de 24ºC ')
              
        elif temperatura_hoy >=26:
            
            for dispositivo in list_dispositivo:

                if dispositivo["tipo"]== 3 :
            
                    dispositivo["temperatura "]= 20
                    
                    return(f'Se prendio automaticamente el {dispositivo["nombre_dispositivo"]} ahora la temperatura es de 20ºC ')
                
#Creamos una funcion para validar si el usuario ingreso un numero entero

def validar_entero(valor):
    
    while valor.isnumeric() == False: 
        
        valor = (input("El valor debe ser un numero entero, intente de nuevo: "))
                                 
    return int(valor)