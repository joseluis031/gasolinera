import threading
import time
import random

#variables
gasolinera = 0
coches = 50

#semáforos
surtidor = threading.Semaphore(1) #solo un coche puede usar el surtidor a la vez(pq solo hay 1 surtidor)
disponible = threading.Semaphore(0) #cuando el coche llega al surtidor, y se baja
acabado = threading.Semaphore(0) #cuando el coche termina de repostar
mutex = threading.Semaphore(1) #para controlar numero de coches


#funcion que simula el repostaje
def repostar(): #falta añadir tipos combustible y tiempos de repostaje y pago
    
    global gasolinera
    global coches
    
    while True:
        surtidor.acquire()
        disponible.release()
        gasolinera = 1
        print ("Repostando el coche {}".format(coches))
        time.sleep(1)

        print ("Repostado el coche {}".format(coches))
        acabado.release()
        coches -= 1
        gasolinera = 0