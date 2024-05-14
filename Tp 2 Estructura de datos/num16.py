from pila import Stack

cola1=Stack()
cola2= Stack()
interseccion= Stack()

cap_v= ["Luke Skywalker","Princess Leia Organa","Han Solo","Chewbacca","Darth Vader","Yoda","Emperor Palpatine","Lando Calrissian","C-3PO","R2-D2","Boba Fett"]
cap_vii= ["Rey","Finn (FN-2187)","Poe Dameron","Kylo Ren (Ben Solo)","Han Solo","Leia Organa","Luke Skywalker",
"Chewbacca","BB-8","Supreme Leader Snoke","Captain Phasma"]

for i in cap_v:
    cola1.push(i)
for i in cap_vii:
    cola2.push(i)

while cola1.size() > 0 and cola2.size() > 0:
    personaje_v = cola1.pop()
    personajes_vii= cola2.elements
    if personaje_v in personajes_vii:
        interseccion.push(personaje_v)



print("Personajes que aparecen en ambos episodios:")
while interseccion.size() > 0:
    print(interseccion.pop())
        

