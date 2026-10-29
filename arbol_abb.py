# Practica: Arbol Binario de Busqueda (ABB)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def insertar(raiz, dato):
    # Un espacio vacio se convierte en un nuevo nodo.
    if raiz is None:
        return Nodo(dato)

    if dato < raiz.dato:
        raiz.izquierdo = insertar(raiz.izquierdo, dato)
    elif dato > raiz.dato:
        raiz.derecho = insertar(raiz.derecho, dato)
    # Si el dato ya existe, no se vuelve a insertar.
    return raiz


def buscar(raiz, dato):
    if raiz is None:
        return False
    if dato == raiz.dato:
        return True
    if dato < raiz.dato:
        return buscar(raiz.izquierdo, dato)
    return buscar(raiz.derecho, dato)


def preorden(raiz):
    if raiz is not None:
        print(raiz.dato, end=" ")  # Raiz, izquierda, derecha.
        preorden(raiz.izquierdo)
        preorden(raiz.derecho)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierdo)
        print(raiz.dato, end=" ")  # Izquierda, raiz, derecha.
        inorden(raiz.derecho)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierdo)
        postorden(raiz.derecho)
        print(raiz.dato, end=" ")  # Izquierda, derecha, raiz.


if __name__ == "__main__":
    # se pueden cambiar estos numeros para probar otro arbol.
    datos = [50, 30, 70, 20, 40, 60, 80]
    raiz = None
    for dato in datos:
        raiz = insertar(raiz, dato)

    print("Datos insertados:", datos)
    print("Preorden:", end=" ")
    preorden(raiz)
    print()
    print("Inorden:", end=" ")
    inorden(raiz)
    print()
    print("Postorden:", end=" ")
    postorden(raiz)
    print()

    for objetivo in [60, 90]:
        resultado = "Encontrado" if buscar(raiz, objetivo) else "No encontrado"
        print("Buscar", objetivo, "->", resultado)
