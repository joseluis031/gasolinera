import threading
import time
import random
#newcatcehpool y newcatchethread
#variables
gasolinera = 0
coches = 50
tiempo = 15
lista_coches = 0

#semáforos
surtidor = threading.Semaphore(1) #solo un coche puede usar el surtidor a la vez(pq solo hay 1 surtidor)
disponible = threading.Semaphore(0) #cuando el coche llega al surtidor, y se baja
acabado = threading.Semaphore(0) #cuando el coche termina de repostar
mutex = threading.Semaphore(1) #para controlar numero de coches


caja = threading.Semaphore(1) #solo una persona puede pagar a la vez
caja_disponible = threading.Semaphore(0) #la persona puede pagar
pagado = threading.Semaphore(0) #la persona termina de pagar
mutex2 = threading.Semaphore(1) #para controlar numero de personas


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
        
#funcion que controla el numero de coches(cola)
def cola_vehiculos():
    
    global coches
    global gasolinera
    global lista_coches
    
    while True:
        mutex.acquire()
        if coches > 0:
            lista_coches += 1
            print ("Coche {} llega al surtidor".format(lista_coches))

            surtidor.release()
            mutex.release()
            disponible.acquire()

            print ("Coche {} esta depositando".format(lista_coches))

            acabado.acquire()
            mutex.acquire()
            coches -= 1
            print("Coche {} ha terminado de repostar".format(lista_coches))
            mutex.release()
            
            
        else:
            print ("No hay coches en la cola")
            mutex.release()
            time.sleep(1)