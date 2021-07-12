import json   #Se importa la libreria

a = {"nombre":"Gabriel", "asignatura":"Técnicas", "vaPerdiendo":True,"notas": [1, 3.5]}  #Se crea un diccionario a - Llave Valor

with open('alumnoGabriel.json', 'w') as f:  #Se abre y se crea automaticamente un archivo .json
   json.dump(a, f)                           #se almacena el json en el archivo


al_gabriel = { "1":"Gabriel","asignatura":"Técnicas","laVaPerdiendo":True, "notasActuales": [1.0, 3.5]}
json_hilera = json.dumps(al_gabriel)         #Serialización metodo dump con s al final de String

with open("alumnoGabriel.json", "r") as f:
   nuevo_alumno = json.load(f)

json_string = """
{
   "1": "Gabriel",
   "asignatura": {
         "1": "qsq"
   },
   "laVaPerdiendo": true,
   "notasActuales": [
         1.0,
         3.5
   ]
}
"""
d = json.loads(json_string)
