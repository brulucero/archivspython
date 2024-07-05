import json
nombres_datos= {}
nombres_datos["jugadores"]= []
nombres_datos["jugadores"].append({"nombre":"pablo" , "apellido":"solari" , "edad":20})
nombres_datos["jugadores"].append({"nombre":"cristian" , "apellido":"zavala" , "edad":24})
nombres_datos["jugadores"].append({"nombre":"dario" , "apellido":"osorio" , "edad":19})
nombres_datos["jugadores"].append({"nombre":"esteban" , "apellido":"paredes" , "edad":42})


with open ("nombres_datos.json","w") as archi:
    json.dump(nombres_datos,archi,indent=4)