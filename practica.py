listaDeCreadores=[]

def menu():
    print(" ")
    print(" ")
    print("=== MENU ===")
    print("1 - registrar creador de contenido")
    print("2 - listar creadores de contenido")
    print("3 - eliminar creadores de contenido")
    print("4 - editar creadores de contenido")
    print("0 - salir")
    print("============")
    print(" ")
    print(" ")
    opcion=input("ingresa una opcion: ")
    return opcion

def registra(lista):
    nombreCreador=input("ingresa el nombre del creador de contenido: ")
    lista.append(nombreCreador)
    
def listar(lista):
    contador=0
    print("=== Lista de creadores de contenido ===")
    while contador<len(lista):
        print(str(contador)+" - "+lista[contador])
        contador+=1

def buscarPorNombre(nombre,lista):
    # esta funcion busca por nomber del creador y retorna el elemento 
    creadorDeContenidoEncontrado="null"
    contador=0
    while contador<len(lista):
        nombreRecoridoLista=lista[contador]
        if(nombre==nombreRecoridoLista):
            creadorDeContenidoEncontrado=nombreRecoridoLista
            break
        contador+=1
    return creadorDeContenidoEncontrado

def buscarPorNombreRPeroetornaElIndice(nombre,lista):
    # esta funcion busca por nomber del creador y retorna el indice 
    indiceDelcreadorDeContenidoEncontrado="null"
    contador=0
    while contador<len(lista):
        nombreRecoridoLista=lista[contador]
        if(nombre==nombreRecoridoLista):
            indiceDelcreadorDeContenidoEncontrado=contador
            break
        contador+=1
    return indiceDelcreadorDeContenidoEncontrado

def eliminar(lista):
    creadorHaBuscar=input("ingresa el nombre del creador a buscar: ")
    nombreDelCreador=buscarPorNombre(creadorHaBuscar,lista)
    if(nombreDelCreador!="null"):
        lista.remove(nombreDelCreador)
        print("nombre eliminado")
    else:
        print("no se a encontrado al recreador de contenido que intento eliminar")

def editar(lista):
    creadorHaBuscar=input("ingresa el nombre del creador a remplazar: ")
    remplazo=input("ingresa el nombre el nombre del creador nuevo: ")
    indiceDelCreador=buscarPorNombreRPeroetornaElIndice(creadorHaBuscar,lista)
    if(indiceDelCreador!="null"):
        lista[indiceDelCreador]=remplazo
        print("nombre remplazado")
    else:
        print("no se a encontrado al recreador de contenido que intento eliminar")


opcion="1"
while opcion!="0":
    opcion=menu()
    if(opcion=="1"):
        registra(listaDeCreadores)
    if(opcion=="2"):
        listar(listaDeCreadores)
    if(opcion=="3"):
        eliminar(listaDeCreadores)
    if(opcion=="4"):
        editar(listaDeCreadores)

print("saliendo del programa")