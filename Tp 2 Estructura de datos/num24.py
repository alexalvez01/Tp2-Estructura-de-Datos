from pila import Stack

pila1=Stack()
pila2=Stack()
pila3=Stack()

personajes = [("Viuda Negra", 2), ("Capitán América", 7), ("Groot", 5), ("Doctor Strange", 10), ("Deadpool", 3), ("Rocket Raccoon", 3),("Iron Man",8),("Hulk",6)]


for personaje in personajes:
    pila1.push(personaje)

contador = 0
pelis_viuda=0
while  pila1.size() > 0:
    personaje=pila1.pop()
    if personaje[0] == "Groot":
        print(f"La posición en la que se encuentra Groot es {contador}")
    if personaje[0] == "Rocket Raccoon":
        print(f"La posición en la que se encuentra Rocket Raccoon es {contador}")
    if personaje[0] == "Viuda Negra":
        pelis_viuda=personaje[1]
    if personaje[0].startswith("C") or personaje[0].startswith("D") or personaje[0].startswith("G"):
        pila3.push(personaje)
    if personaje[1]>5:
        pila2.push(personaje)
    contador+=1
    

print("Los personajes que participaron en mas de 5 películas son:")
while pila2.size() > 0:
    personaje=pila2.pop()
    print(f"-{personaje[0]}")
print(f"Viuda Negra participo en {pelis_viuda} películas")
print("Los personajes que empiezan por C, D y G son:")
while pila3.size() > 0:
    personaje=pila3.pop()
    print(f"-{personaje[0]}")