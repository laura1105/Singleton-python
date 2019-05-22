import threading

class A:
    _instance = None

    def foo(self):
        return id(self)

def Singleton(klass):
    if not klass._instance:
        klass._instance = klass()
    return klass._instance

class B(A):
    _instance = None


class C(A):
    _instance = None

def clase(klass, num_hilo):
    b = Singleton(klass)
    a = str(id(b)) + " " + str(b.foo()) + " numero de hilo " + str(num_hilo)
    print(a)

def hilo_1():
    contador = 0
    while contador < 10:
        contador += 1
        clase(A, 1)

def hilo_2():
    contador = 0
    while contador < 10:
        contador += 1
        clase(B, 2)

def hilo_3():
    contador = 0
    while contador < 10:
        contador += 1
        clase(C, 3)

def hilo_4():
    contador = 0
    while contador < 10:
        contador += 1
        clase(A, 4)


threading.Thread(target=hilo_1).start()
threading.Thread(target=hilo_2).start()
threading.Thread(target=hilo_3).start()
threading.Thread(target=hilo_4).start()
