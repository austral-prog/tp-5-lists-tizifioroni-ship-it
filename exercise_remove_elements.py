# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """

    if len(lista) > 5:
        lista.pop(5)

    if len(lista) > 4:
        lista.pop(4)

    if len(lista) > 0:
        lista.pop(0)

    return lista