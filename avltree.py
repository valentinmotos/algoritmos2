class AVLTree:
	root = None

class AVLNode:
      parent = None
      leftnode = None
      rightnode = None
      key = None
      value = None
      bf = None
      height = None #atributo para guardar las alturas de cada nodo

def mostrar_arbol(node, nivel=0, prefijo="Raíz: "):
    """Muestra el árbol AVL en consola."""
    if node is not None:
        print(" " * (nivel * 4) + prefijo + f"[Clave: {node.key}, Valor: {node.value}, BF: {node.bf}]")
        mostrar_arbol(node.leftnode, nivel + 1, "Izq: ")
        mostrar_arbol(node.rightnode, nivel + 1, "Der: ")

def rotate_right(tree, avlnode):
      new_root = avlnode.leftnode
      avlnode.leftnode = new_root.rightnode

      if new_root.rightnode != None:
            new_root.rightnode.parent = avlnode
      new_root.parent = avlnode.parent

      if avlnode.parent == None:
            tree.root = new_root
      else:
            if avlnode.parent.rightnode == avlnode:
                  avlnode.parent.rightnode = new_root
            else:
                  avlnode.parent.leftnode = new_root
      new_root.rightnode = avlnode
      avlnode.parent = new_root

      return tree.root


def rotate_left(tree,avlnode):

      new_root = avlnode.rightnode
      avlnode.rightnode = new_root.leftnode

      if new_root.leftnode != None:
            new_root.leftnode.parent = avlnode
      new_root.parent = avlnode.parent

      if avlnode.parent == None:
            tree.root = new_root
      else:
            if avlnode.parent.leftnode == avlnode:
                  avlnode.parent.leftnode = new_root
            else:
                  avlnode.parent.rightnode = new_root
      new_root.leftnode = avlnode
      avlnode.parent = new_root              

      return tree.root

def calculateBalance(AVL):

      if AVL is None:
            return -1
      
      altura_derecha = calculateBalance(AVL.rightnode)
      altura_izquierda = calculateBalance(AVL.leftnode)
      
      AVL.height =  1 + max(altura_derecha,altura_izquierda)

      AVL.bf = altura_izquierda - altura_derecha

      return AVL

def reBalanceR(node):
    if node is None:
        return None

    # Primero rebalanceamos los hijos
    node.leftnode = reBalanceR(node.leftnode)
    node.rightnode = reBalanceR(node.rightnode)

    calculateBalance(node)

    if node.bf > 1:      
        node = rotate_left(node)
    elif node.bf < -1:     
        node = rotate_right(node)

    return node 

def reBalance(tree):
    if tree and tree.root:
        tree.root = reBalanceR(tree.root)

def insertAVL(Tree):
     insert(Tree,Tree.value, Tree.key) #insert de binarytree.py
     reBalance(Tree)

def deleteAVL(Tree):
      delete(Tree,Tree.value,Tree.key) #delete de binarytree.py


if __name__ == '__main__':
 
      from binarytree import *

