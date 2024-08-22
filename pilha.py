class Pilha:

    def __init__(self, max_size):
     self.items = []
     self.max_size = max_size

def push(self, item):
    self.items.append(item)   
    if len(self.items) >= self.max_size:
        print("Pilha cheia")
    else:
        self.items.append(item)

def pop(self):
    if self.is_empty:
        print("Pilha vazia")
        return
    else:   
        self.items.pop()


def peek(self):
    return self.items[-1] if self.items else None

def is_empty(self):
    return len(self.items) == 0

def main():
    max_size = input("Digite o tamanho da pilha maxima")
    pilha = Pilha(max_size)

    while True:
        print("ESCOLHA UMA DAS FUNÇÕES: ")
        print("1. Adicionar a pilha ")
        print("2. Remover da pilha ")
        print("3. Ver topo da pilha ")
        print("4. Verificar se a pilha esta vazia ")
        print("5. Sair")

        escolha = input("Escolha a tarefa desejada: ")

        if escolha == "1":
            item = input("Digite o que quer colocar na pilha: ")
            pilha.push(item)        

        elif escolha == "2":
            item_removido = pilha.pop()

        elif escolha == "3":
            topo = pilha.peek
            if topo is not None:
                print("Elemento que esta no topo é: {topo}")
            else:
                print("Pilha vazia")

        elif escolha == "4":
            if pilha.is_empty():
                print("A pilha esta vazia")
            else:
                print("A pilha não esta vazia")

        elif escolha == "5":
            break
        else:
            print("Opção invalida.")
            
        
            


