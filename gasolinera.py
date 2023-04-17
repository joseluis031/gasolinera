import threading
import time
import random
#newcatcehpool y newcatchethread
#variables
gasolinera = 0
coches = 50
tiempo = 15 #a ver como lo incluyo al final
lista_coches = 0
caja = 0

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
        print ("\nRepostando el coche {}".format(coches))
        time.sleep(1)

        print ("\nRepostado el coche {}".format(coches))
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
            print ("\nCoche {} llega al surtidor".format(lista_coches))

            surtidor.release()
            mutex.release()
            disponible.acquire()

            print ("\nCoche {} esta depositando".format(lista_coches))

            acabado.acquire()
            mutex.acquire()
            coches -= 1
            print("\nCoche {} ha terminado de repostar".format(lista_coches))
            mutex.release()
            
            
        else:
            print ("\nNo hay coches en la cola")
            mutex.release()
            time.sleep(1)
            
def pagar(): #puede ser que sea mejor meterlo todo en una funcion, y que la funcion sea la q realice todo
    
    global caja
    global lista_coches
    
    while True:
        caja.acquire()
        caja_disponible.release()
        caja = 1
        print ("\nPagando la persona del coche {}".format(lista_coches))
        time.sleep(1)

        print ("\nPagado la persona del coche {}".format(lista_coches))
        pagado.release()
        lista_coches -= 1
        caja = 0
        print("\nEl coche {} se va de la gasolinera".format(lista_coches))
        
def cola_personas():
    
    
    global lista_coches
    global caja
    
    while True:
        mutex2.acquire()
        if lista_coches > 0:
            lista_coches += 1
            print ("\nPersona del coche {} llega a la caja".format(lista_coches))

            caja.release()
            mutex2.release()
            caja_disponible.acquire()

            print ("\nPersona del coche {} esta pagando".format(lista_coches))

            pagado.acquire()
            mutex2.acquire()
            lista_coches -= 1
            print("\nPersona del coche {} ha terminado de pagar".format(lista_coches))
            mutex2.release()
            
            
        else:
            print ("\nNo hay personas en la cola de la caja")
            mutex2.release()
            time.sleep(1)
            
            
def main():
    
    #creamos los hilos
    hilo_repostar = threading.Thread(target=repostar)
    hilo_pagar = threading.Thread(target=pagar)

    hilo_repostar.start()
    hilo_pagar.start()
    
    while True:
        
        hilo_cola_vehiculos = threading.Thread(target=cola_vehiculos)
        hilo_cola_personas = threading.Thread(target=cola_personas)

        hilo_cola_vehiculos.start()
        hilo_cola_personas.start()
        
        time.sleep(10)
        
#no se me inicia el hilo de la caja, tengo que pensar el por que