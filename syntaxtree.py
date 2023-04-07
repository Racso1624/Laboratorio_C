# Oscar Fernando López Barrios
# Carné 20679

from regex import *

# Clase Syntax Tree
class SyntaxTree(object):

    # Se inicia con la expresion regular
    def __init__(self, regex):
        self.regex = regex
        # Se agrega la raiz al final de la expresion
        self.postfix =  Regex(self.regex).postfix_expression
        self.postfix.append("#")
        self.postfix.append(".")
        self.node_list = []
        self.tree_root = None
        self.buildTree()
        self.printTree()

    # Se crea la clase para realiza el arbol
    def buildTree(self):
        
        # Se inicia el stack con los nodos
        node_stack = []
        position_counter = 1

        # Se itera en cada caracter de la expresion
        print(self.postfix)
        for character in self.postfix:
            # Si es unario solo se crea el hijo a la izquierda
            if(isinstance(character, str) and character in "+*?"):
                new_node = Node(character)
                new_node.left_child = node_stack.pop()
                node_stack.append(new_node)
                self.node_list.append(new_node)
            # Si es binario se crean los hijos de izquierda y derecha
            elif(isinstance(character, str) and character in ".|"):
                new_node = Node(character)
                new_node.right_child = node_stack.pop()
                new_node.left_child = node_stack.pop()
                node_stack.append(new_node)
                self.node_list.append(new_node)
            # Si es un simbolo solo se guarda en el stack
            else:
                new_node = Node(character, position_counter)
                node_stack.append(new_node)
                self.node_list.append(new_node)
        
        # Cuando se termina el for la raiz queda en el stack
        self.tree_root = node_stack.pop()

    # Funcion para imprimir caracteres y sus nodos hijos
    def printTree(self):
        # Para cada nodo en la lista de los nodos
        for node in self.node_list:\
            # Se imprime el caracter
            print("Caracter")
            print(node.character)
            # Si tiene hijos izquierdos y derechos se imprimen
            if(node.left_child):
                print("Izquierdo")
                print(node.left_child.character)
            if(node.right_child):
                print("Derecho")
                print(node.right_child.character)
    
    def graphTree(self):
        pass


# Se crea la clase nodo
class Node(object):
    
    # Se inicia con el caracter y la posicion de manera nula
    def __init__(self, character, position = None):
        # Se guardan los datos de cada nodo con respecto a su pos
        self.character = character
        self.firstpos = set()
        self.lastpos = set()
        self.followpos = set()
        self.position = position
        # Para cada nodo se guardan sus hijos
        self.left_child = None
        self.right_child = None