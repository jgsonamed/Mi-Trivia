BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import random
puntaje = random.randint (0,100)

import time
iniciar_trivia = True
intentos = 0

print("\033[33m¡Bienvenido a mi trivia sobre GHOST9!\033[39m")

time.sleep(2)
print("\033[32m Pon aprueba tu perspicacia :D \n\033[39m")
time.sleep(2)
print("\033[34mComenzarás con:\033[39m",puntaje,"puntos")
time.sleep(2)
nombre=input("\033[34mEscribe tu nombre:\033[39m")

print("\033[34m\nHey\033[39m",nombre,"\033[34m¿Estas Listo?\033[39m\n")
time.sleep(2)
print("\033[32m¡Observa y Deduce!\n\033[39m")
time.sleep(2)
print("\033[34mResponde las siguientes preguntas escribiendo la letra minuscula de la alternativa y presiona ENTER para enviar tu respuesta:\n\033[39m")

time.sleep(2)
while iniciar_trivia == True: 
   intentos += 1
   print("\n\033[35mIntento número:", intentos)
   input("Presiona Enter para continuar\033[39m")
   print("\n\033[33m1)¿Cuál es la traduccion al español de 'GHOST9'? \033[39m\n")
   
   alternativa = ["a)Electro9","b)grupo9","c)fantasma9","d)talento9"]
   for number in range(0,4):
    print("\033[36m",alternativa[number],"\033[39m")
     
   respuesta_1= input("\n\033[34mtu respuesta: ")
   while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:\033[39m")
   
   if respuesta_1== "c":
     puntaje= puntaje + 20
     print("\033[33mCorrecto :) tienes\033[39m",puntaje,"\033[33mpuntos.\033[39m")
    
   else:
    print("\033[31mFALLASTE\033[39m")
   time.sleep(2)

   print("\n\033[32m¡Vamos por la segunda!\033[39m\n")
   time.sleep(2)
   print("\033[33m2)¿Cómo se llama su fandom de GHOST9?\033[39m\n")
   alternativa_2 = ["a)Ghostie","b)fan","c)yes","d)sol"]
   for number in range(0,4):
    print("\033[36m",alternativa_2[number],"\033[39m")

   respuesta_2= input("\n\033[34mtu respuesta: ")
   while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \033[39m")
   if respuesta_2== "a":
     puntaje= puntaje + 20
     print("\033[33mExcelente llevas\033[39m",puntaje,"\033[33mpuntos.\033[39m")
    
   else:
    print("\033[31mFALLASTE\033[39m")

   time.sleep(3)
  
   print("\n\033[32mÚltima pregunta\033[329m,\033[35m ¡Tú puedes!\033[35m\n")
   time.sleep(2)
   print("\033[33m3)¿Cuántas canciones tiene GHOST9?\033[39m\n")
   alternativa_3 = ["a)1","b)9","c)ninguna ,solo hacen covers","d)37"]
   for number in range(0,4):
    print("\033[36m",alternativa_3[number],"\033[39m")

   respuesta_3= input("\n\033[34mtu respuesta: ")
   while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \033[39m")
    
   if respuesta_3== "a":
    print("\033[31mIncorrecto. GHOST9 tiene 6 albunes musicales\033[39m")
    puntaje= puntaje -7
   elif respuesta_3== "b":
    print("\033[31mIncorrecto. 9 es muy poco para su variada discografia\033[39m")
    puntaje= puntaje /9
   elif respuesta_3== "c":
    print("\033[31mIncorrecto. GHOST9 ha sacado varias canciones desde el 2020\033[39m")
    puntaje= puntaje * 0
   else:
    print("\033[33m\n¡WOW!",nombre,"Acertaste\033[39m")
    puntaje= puntaje + 20
   time.sleep(2)
   print("\nGracias por jugar mi trivia, obtuviste",puntaje,"de puntaje.")
   time.sleep(1)

   print("\033[35m\n¿Deseas intentar la trivia nuevamente?")
   repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: \033[39m").lower()
   import random
   puntaje = random.randint (0,100)
   print("\n\033[34mComenzarás con:",puntaje,"puntos")

if repetir_trivia != "si":
   
   print("\nEspero que te hayas divertido, hasta pronto!")
   iniciar_trivia = False