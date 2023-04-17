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