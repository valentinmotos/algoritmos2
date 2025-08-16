class BinaryTree:
  root = None


class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None


class LinkedList:
  head = None


class Node:
  value = None
  nextNode = None


def searchR(node, element):

  if node == None:
    return None
  if node.value == element:
    return node.key
  searchleft = searchR(node.leftnode, element)
  if searchleft != None:
    return searchleft

  return searchR(node.rightnode, element)


def search(B, element):

  return searchR(B.root, element)


def insertR(newNode, currentNode):
  if newNode.key != currentNode.key:
    if newNode.key > currentNode.key:
      if currentNode.rightnode == None:
        currentNode.rightnode = newNode
        newNode.parent = currentNode
      else:
        insertR(newNode, currentNode.rightnode)
    else:
      if currentNode.leftnode == None:
        currentNode.leftnode = newNode
        newNode.parent = currentNode
      else:
        insertR(newNode, currentNode.leftnode)
  else:
    return None


def insert(B, element, key):

  newNode = BinaryTreeNode()
  newNode.value = element
  newNode.key = key

  if B.root == None:
    B.root = newNode
  else:
    insertR(newNode, B.root)
  #print("inserta")
  return search(B, element)


def deleteR(currentNode, key, B):

  if currentNode.key == key:
    if currentNode.parent == None:
      print("Se quiere eliminar la raiz")
      if currentNode.leftnode != None and currentNode.rightnode != None:
        print("La raiz es una rama con dos hijos")
        print("currentNode ", currentNode.value)
        currentNode2 = currentNode.rightnode
        k = 0

        while currentNode2.leftnode != None:
          currentNode2 = currentNode2.leftnode
          k = k + 1

        Padre = currentNode2.parent
        print("currentNode2 ", currentNode2.value)
        print("padre.value", Padre.value)
        if k != 0:
          Padre.leftnode = None
        else:
          Padre.rightnode = None

        B.root = currentNode2
        Padre2 = currentNode.parent
        currentNode2.leftnode = currentNode.leftnode
        currentNode2.rightnode = currentNode.rightnode

    elif currentNode.leftnode != None and currentNode.rightnode != None:
      print("Es una rama con dos hijos")

      currentNode2 = currentNode.rightnode
      k = 0

      while currentNode2.leftnode != None:
        currentNode2 = currentNode2.leftnode
        k = k + 1

      Padre = currentNode2.parent

      if k != 0:
        Padre.leftnode = None
      else:
        Padre.rightnode = None

      Padre2 = currentNode.parent

      if Padre2.key > key:
        Padre2.leftnode = currentNode2
        currentNode2.leftnode = currentNode.leftnode
        currentNode2.rightnode = currentNode.rightnode
      else:
        Padre2.rightnode = currentNode2
        currentNode2.leftnode = currentNode.leftnode
        currentNode2.rightnode = currentNode.rightnode

    elif currentNode.leftnode != None or currentNode.rightnode != None:
      print("Rama con una hoja")

      Padre = currentNode.parent

      if currentNode.leftnode == None:
        Hijo = currentNode.rightnode
        currentNode.rightnode = None
      else:
        Hijo = currentNode.leftnode
        currentNode.leftnode = None

      if Padre.leftnode == currentNode:
        Padre.leftnode = Hijo
      else:
        Padre.rightnode = Hijo

    else:

      print("Es una hoja")
      padreHoja = currentNode.parent
      print(padreHoja.key)

      if padreHoja.leftnode == currentNode:
        padreHoja.leftnode = None
      else:
        padreHoja.rightnode = None

  else:

    if key < currentNode.key:
      deleteR(currentNode.leftnode, key, B)
    else:
      deleteR(currentNode.rightnode, key, B)

  return key


def delete(B, element):
  key = search(B, element)

  if key == None:
    return None
  else:
    return deleteR(B.root, key, B)


def searchKeyR(node, key):

  if node == None:
    return None
  if node.key == key:
    return node.key
  searchleft = searchKeyR(node.leftnode, key)
  if searchleft != None:
    return searchleft

  return searchKeyR(node.rightnode, key)


def searchKey(B, key):

  return searchKeyR(B.root, key)


def deleteKey(B, key):

  ekey = searchKey(B, key)

  if ekey == None:
    return None
  else:
    return deleteR(B.root, key)



def accessR(node, key):

  if node == None:
    return None
  else:
    if node.key == key:
      return node.value
    elif key < node.key:
      #print("por izquierda")
      return accessR(node.leftnode, key)
    elif key > node.key:
      #print("por derecha")
      return accessR(node.rightnode, key)
    else:
      return None


def access(B, key):

  return accessR(B.root, key)


def updateR(node, key, element):

  if node == None:
    return None
  else:
    if node.key == key:
      node.value = element
      return node.key
    elif key < node.key:
      #print("por izquierda")
      return updateR(node.leftnode, key, element)
    elif key > node.key:
      #print("por derecha")
      return updateR(node.rightnode, key, element)
    else:
      return None


def update(B, element, key):

  return updateR(B.root, key, element)



def mostrar(l):
  current = l.head
  k = 0
  if len(l) == 1:
    print("LINKEDLIST: [",current.value, end = " ] ")
  else:
    while current != None:
      if k == 0:
        print("LINKEDLIST: [",current.value, end = " ")
      elif k == (len(l) - 1):
        print(current.value, end = " ] ")
      else:
        print(current.value, end = " ")
      current = current.nextNode
      k = k + 1
  print(" ")

def añadeAlFinal(l, element):
  currentNode = l.head
  newNode = Node()
  newNode.value = element

  if currentNode == None:
    l.head = newNode
  else:
    while currentNode.nextNode != None:
      currentNode = currentNode.nextNode

    currentNode.nextNode = newNode

  return l


def traverseInOrderR(node, l):

  if node != None:

    traverseInOrderR(node.leftnode, l)
    añadeAlFinal(l, node.key)
    traverseInOrderR(node.rightnode, l)
  else:
    return None


def traverseInOrder(B):

  listaInOrder = LinkedList()

  return traverseInOrderR(B.root, listaInOrder), mostrar(listaInOrder)



def traversePostOrderR(node, l):

  if node != None:

    traversePostOrderR(node.leftnode, l)
    traversePostOrderR(node.rightnode, l)
    añadeAlFinal(l, node.key)
  else:
    return None


def traverseInPostOrder(B):
  listaPostOrder = LinkedList()

  return traversePostOrderR(B.root, listaPostOrder), mostrar(listaPostOrder)

def traversePreOrderR(node, l):

  if node != None:
    añadeAlFinal(l, node.key)
    traversePreOrderR(node.leftnode, l)
    traversePreOrderR(node.rightnode, l)
  else:
    return None


def traverseInPreOrder(B):
  listaPreOrder = LinkedList()

  return traversePreOrderR(B.root, listaPreOrder), mostrar(listaPreOrder)


def añadeAlFinal(l, element):
  currentNode = l.head
  newNode = Node()
  newNode.value = element

  if currentNode == None:
    l.head = newNode
  else:
    while currentNode.nextNode != None:
      currentNode = currentNode.nextNode

    currentNode.nextNode = newNode

  return l


def traverseBreadFirstR(node, l):

  if node != None:
    añadeAlFinal(l, node.key)

  else:
    return None

  if node.leftnode != None:
    traverseBreadFirstR(node.leftnode, l)
  elif node.rightnode != None:
    traverseBreadFirstR(node.rightnode, l)


def traverseBreadFirst(B):
  listaBFOrder = LinkedList()

  return traverseBreadFirstR(B.root, listaBFOrder), mostrar(listaBFOrder)