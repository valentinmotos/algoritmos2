class AVLTree:
	root = None

class AVLNode:
        parent = None
        leftnode = None
        rightnode = None
        key = None
        value = None
        bf = None


# rotateRight(Tree,avlnode) 
# Descripción: Implementa la operación rotación a la derecha 
# Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
# Salida: retorna la nueva raíz

def mostrar_arbol(node, nivel=0, prefijo="Raíz: "):
    """Muestra el árbol AVL en consola."""
    if node is not None:
        print(" " * (nivel * 4) + prefijo + f"[Clave: {node.key}, Valor: {node.value}, BF: {node.bf}]")
        mostrar_arbol(node.leftnode, nivel + 1, "Izq: ")
        mostrar_arbol(node.rightnode, nivel + 1, "Der: ")

def rotate_right(tree, avlnode):
      
      if tree == None:
            return None
      elif avlnode.bf > 1:
            if avlnode.leftnode.rightnode != None:
                tree.root = avlnode.leftnode
                avlnode.parent = 
                  
      
        


if __name__ == '__main__':
        from algo1 import *

        T = AVLTree()
        nodeE = AVLNode()
        T.root = nodeE
        nodeE.value = 'E'
        nodeE.bf = 2

        nodeC = AVLNode()
        nodeC.bf = 1
        nodeC.value = 'C'
        nodeE.leftnode = nodeC
        nodeE.value = 'E'
        nodeE.bf = 2

        nodeF = AVLNode()
        nodeF.value = 'F'
        nodeE.rightnode = nodeF
        nodeF.bf = 0

        nodeB = AVLNode()
        nodeB.value = 'B'
        nodeC.leftnode = nodeB
        nodeC.value = 'C'
        nodeB.bf = 1

        nodeD = AVLNode()
        nodeD.value = 'D'
        nodeC.rightnode = nodeD
        nodeD.bf = 0

        nodeA = AVLNode()
        nodeA.value = 'A'
        nodeB.leftnode = nodeA
        nodeA.bf = 0

        print()
        mostrar_arbol(T.root)
        print()
        print("-------ROTATE RIGHT------")
        rotate_left(T.root, nodeE)
