# Librerias
from random import choice # Escoger letra aleatoria
import pandas as pd # Tabular
import time # calcula el tiempo

print("**********************¡Bienvenid@ a tu juego de stop virtual!***************************")
print("")
Nombre = str(input("Escribe tu nombre: "))
print("")
print("Hola",Nombre,",\nA continuacion te mostraremos las reglas del juego")
print("")
print("Reglas:")
print("1. El juego te dara una letra aleatoria, por cada una de estas, deberas escribir una palabra que inicie con dicha letra segun corresponda en cada casilla.")
print("2. Por cada palabra corecta se le asignara 100 puntos.")
print("3. Por cada palabra incorecta se le quitara 100 puntos.")
print("4. Si no pone nada, quedara igual.") 
print("******************************************************************************************")
opcion= (input("¿Desea continuar, responda con un si o no en minuscula?: "))

if opcion=="si":
 Partidas = int(input("¿Cuantas partidas quieres jugar?: "))
 print("")
 print("******************************************************************************************")
 print("                                 inicio de juego                                       ")
 print("******************************************************************************************")

 letras= ['A','B','C','D','E','F','G','I','J','L','N','P','O','R','S','T']
 letra=choice(letras)
 LETRA=[]
 NOMBRE =[]
 APELLIDO=[]
 LUGAR =[]
 ANIMAL=[]
 FRUTA=[]
 COLOR=[]
 OBJETO=[]
 TIEMPO=[]
 PUNTAJE=[]
   
 puntaje = 0
 def Puntaje(palabra):
    global puntaje
    if len(palabra)>=3 and palabra[0].upper()!= letra:
      puntaje -=100
    if len(palabra)>=3 and palabra [0].upper()== letra:
      puntaje +=100
      return puntaje

 PuntajePartida = 0     
 puntajetotal = 0
 sumatiempo = 0 
 for i in range(Partidas):

  if puntaje > 0:
    puntaje ==0 
  else:
    print("")
  letra=choice(letras) 
  print(f"La cantidad de partidas son: {Partidas}")
  print("")
  print(f"La letra es {letra}")
  inicio=time.time() # Variable de inicio de tiempo
  ##############################################
  nombre=input("Ingrese el nombre: ")
  apellido=input("Ingrese un apellido: ")
  lugar=input("Ingrese un lugar: ")
  animal=input("Ingrese un animal: ")
  fruta=input("Ingrese una fruta: ")
  color=input("Ingrese un color: ")
  objeto=input("Ingrese un objeto: ")
  ##############################################
  final=time.time() # variable de fin de tiempo
  tiempo=round(final-inicio,0)# Calcular cuanto tiempo transcurrido durante una partida
  

  respuestas= [nombre,apellido,lugar,animal,fruta,color,objeto]

  for j in respuestas:
    if j=="":
      puntaje==0             
    else:      
      Puntaje(j)
      
  sumatiempo = sumatiempo + tiempo #Suma de tiempo final
  puntajetotal = puntajetotal + puntaje # Suma puntaje total
  LETRA.append(letra)
  NOMBRE.append(nombre)
  APELLIDO.append(apellido)
  LUGAR.append(lugar)
  ANIMAL.append(animal)
  FRUTA.append(fruta)
  COLOR.append(color)
  OBJETO.append(objeto)
  TIEMPO.append(tiempo)
  PUNTAJE.append(puntaje)
  print(f"- Su puntaje de parida fue: {puntaje}")
  print(f"- Su tiempo de parida fue: {tiempo}")
  print("**************************************************************************************")
  if puntaje >= 0:
     puntaje = 0 
     
      

  
  
 print("****************************************************************************************")

 df=pd.DataFrame({"LETRA":LETRA,"NOMBRE":NOMBRE,"APELLIDO":APELLIDO,"LUGAR":LUGAR,"ANIMAL":ANIMAL,"FRUTA":FRUTA,"COLOR":COLOR,"OBJETO":OBJETO,"TIEMPO":TIEMPO,"PUNTAJE": PUNTAJE})
 print("                                 TABAL DE RESULTADOS                                    ")
 print("****************************************************************************************")
 print(df)
 print("****************************************************************************************")
 print("")
 print("- Su tiempo total  es: ", sumatiempo)
 print("")
 puntajetotal = puntajetotal + puntaje
 print("- Su puntaje total es: ", puntajetotal)
 print ("")
 print("FIN DEL JUEGO :)")
else:
  print("FIN DE LA PARTIDA")

