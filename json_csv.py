import json

a = {"nombre": "Gabriel",
     "asignatura": "Matematicas",
     "vaPerdiendo": True,
     "notas": [1, 3.5]}

with open("alumnoGabriel.json",'w') as f:
    json.dump(a,f)

al_gabriel = {"1": "Gabriel", "asignatura":"matematica","laVaPerdiendo":True,"notasActuales":[1.0,3.5]}
json_hilera = json.dumps(al_gabriel)

with open('alumnoGabriel.json', 'r') as f:
    nuevo_alumno = json.load(f)

with open('movies.json', 'r', encoding="utf-8") as f:
    movies = json.load(f)

json_string = """{"1": "Gabriel", "asignatura": "matematica", "laVaPerdiendo": true, "notasActuales": [1.0, 3.5]}"""
d= json.loads(json_string)
