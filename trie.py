class Trie:
  root = None

class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

def mostrar_trie(node, nivel=0):
    if node is None:
        return

    indentacion = "  " * nivel
    fin = " (Fin)" if node.isEndOfWord else ""
    print(f"{indentacion}{node.key}{fin}")

    if node.children is not None:
        actual = node.children.head
        while actual is not None:
            mostrar_trie(actual.value, nivel + 1)
            actual = actual.nextNode


def insertR(trie_node, element):
  if len(element) == 0:
    trie_node.isEndOfWord = True
    return
  
  letra = element[0]

  if trie_node.children != None:
    current_node = trie_node.children.head

    while current_node != None:

      if current_node.value.key == letra:
        trie_node = current_node.value
        break
      current_node = current_node.nextNode

    if current_node == None:
      new_node = TrieNode()
      new_node.key = letra
      new_node.parent = trie_node

      add(trie_node.children, new_node)
      trie_node = new_node

  else:
    trie_node.children = LinkedList()
    new_node = TrieNode()
    new_node.key = letra
    new_node.parent = trie_node
    
    add(trie_node.children, new_node)
    trie_node = new_node

  element = element[1:]
  return insertR(trie_node, element)

def insert_trie(T, palabra):
  if T.root != None:
    insertR(T.root, palabra)
  else:
    root = TrieNode()
    root.key = None
    T.root = root
    return insert_trie(T, palabra)

def searchR(trie_node, element):
  if len(element) == 0:
      return trie_node.isEndOfWord #si encontré todos los caracteres entonces tengo que verificar que sea un fin de palabra

  letra = element[0]

  if trie_node.children is not None:
      current_node = trie_node.children.head
      found = False

      while current_node is not None:
          if current_node.value.key == letra:
              trie_node = current_node.value
              found = True
              break
          current_node = current_node.nextNode

      if not found:
          return False

      return searchR(trie_node, element[1:])
  else:
      return False

def search_trie(T, element):
   if T.root:
      return searchR(T.root, element)
   return False 


# delete(T,element)
# Descripción: Elimina un elemento se encuentre dentro del Trie
# Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
# Salida: Devuelve False o True  según se haya eliminado el elemento.

def delete_with_one_child(value_to_find,trie_node):
  current_node = trie_node.parent
  while current_node is not None:
    if current_node.value.key == value_to_find:
      current_node.parent = None
      return True
      
   
def deleteR(trie_node, element):

  if len(element)!=0:
     
    letra = element[0]
    if trie_node.children is not None:
     
      current_node = trie_node.children.head
      while current_node:
          if current_node.value.key == letra:

            if length(trie_node.children)>1: #eliminar a partir de estos keys
              two_or_more_childrens = current_node.value.key
            else:
              value_to_find = current_node.value.key

            trie_node = current_node.value
            
            
            break
          current_node = current_node.nextNode
  
    return deleteR(trie_node, element[1:])
  else:
    delete_with_one_child(value_to_find,trie_node)
     
  return 

def delete_trie(T,element):
  if search_trie(T,element) is not False and T.root is not None: 
    deleteR(T.root,element)  
  return False



from linkedlist import *

T = Trie()
T.root = None

insert_trie(T, "Valentin")
insert_trie(T, "Vacaciones")
insert_trie(T, "bien")
insert_trie(T,"bienvenido")
insert_trie(T,"caso")
mostrar_trie(T.root)
print(delete_trie(T, "caso"))
