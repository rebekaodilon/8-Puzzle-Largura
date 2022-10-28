import argparse
import time
import timeit
from collections import deque

class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)    

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None 
NosExpandidos = 0 
MaxSearchDeep = 0 
MaxFrontier = 0 

def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        no = Queue.popleft()
        boardVisited.add(no.map)
        if no.state == GoalState:
            GoalNode = no
            return Queue
        posiblePaths = subNos(no)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize

values_0 = [0,1,2,1,2,3,2,3,4]
values_1 = [1,0,1,2,1,2,3,2,3]
values_2 = [2,1,0,3,2,1,4,3,2]
values_3 = [1,2,3,0,1,2,1,2,3]
values_4 = [2,1,2,1,0,1,2,1,2]
values_5 = [3,2,1,2,1,0,3,2,1]
values_6 = [2,3,4,1,2,3,0,1,2]
values_7 = [3,2,3,2,1,2,1,0,1]
values_8 = [4,3,2,3,2,1,2,1,0]

def Heuristic(no):

    global values_0,values_1,values_2,values_3,values_4,values_5,values_6,values_7,values_8   
    v0=values_0[no.index("0")]
    v1=values_1[no.index("1")]
    v2=values_2[no.index("2")]
    v3=values_3[no.index("3")]
    v4=values_4[no.index("4")]
    v5=values_5[no.index("5")]
    v6=values_6[no.index("6")]
    v7=values_7[no.index("7")]
    v8=values_8[no.index("8")]
    valorTotal = v0+v1+v2+v3+v4+v5+v6+v7+v8
    return valorTotal
    
        

    
def subNos(no):

    global NosExpandidos
    NosExpandidos = NosExpandidos+1

    proxCaminho = []
    proxCaminho.append(PuzzleState(move(no.state, 1), no, 1, no.depth + 1, no.cost + 1, 0))
    proxCaminho.append(PuzzleState(move(no.state, 2), no, 2, no.depth + 1, no.cost + 1, 0))
    proxCaminho.append(PuzzleState(move(no.state, 3), no, 3, no.depth + 1, no.cost + 1, 0))
    proxCaminho.append(PuzzleState(move(no.state, 4), no, 4, no.depth + 1, no.cost + 1, 0))
    nos=[]
    for procPaths in proxCaminho:
        if(procPaths.state!=None):
            nos.append(procPaths)
    return nos

def move(estado, direcao):
    novoEstado = estado[:]
    
    index = novoEstado.index(0)

    if(index==0):
        if(direcao==1):
            return None
        if(direcao==2):
            temp=novoEstado[0]
            novoEstado[0]=novoEstado[3]
            novoEstado[3]=temp
        if(direcao==3):
            return None
        if(direcao==4):
            temp=novoEstado[0]
            novoEstado[0]=novoEstado[1]
            novoEstado[1]=temp
        return novoEstado      
    if(index==1):
        if(direcao==1):
            return None
        if(direcao==2):
            temp=novoEstado[1]
            novoEstado[1]=novoEstado[4]
            novoEstado[4]=temp
        if(direcao==3):
            temp=novoEstado[1]
            novoEstado[1]=novoEstado[0]
            novoEstado[0]=temp
        if(direcao==4):
            temp=novoEstado[1]
            novoEstado[1]=novoEstado[2]
            novoEstado[2]=temp
        return novoEstado    
    if(index==2):
        if(direcao==1):
            return None
        if(direcao==2):
            temp=novoEstado[2]
            novoEstado[2]=novoEstado[5]
            novoEstado[5]=temp
        if(direcao==3):
            temp=novoEstado[2]
            novoEstado[2]=novoEstado[1]
            novoEstado[1]=temp
        if(direcao==4):
            return None
        return novoEstado
    if(index==3):
        if(direcao==1):
            temp=novoEstado[3]
            novoEstado[3]=novoEstado[0]
            novoEstado[0]=temp
        if(direcao==2):
            temp=novoEstado[3]
            novoEstado[3]=novoEstado[6]
            novoEstado[6]=temp
        if(direcao==3):
            return None
        if(direcao==4):
            temp=novoEstado[3]
            novoEstado[3]=novoEstado[4]
            novoEstado[4]=temp
        return novoEstado
    if(index==4):
        if(direcao==1):
            temp=novoEstado[4]
            novoEstado[4]=novoEstado[1]
            novoEstado[1]=temp
        if(direcao==2):
            temp=novoEstado[4]
            novoEstado[4]=novoEstado[7]
            novoEstado[7]=temp
        if(direcao==3):
            temp=novoEstado[4]
            novoEstado[4]=novoEstado[3]
            novoEstado[3]=temp
        if(direcao==4):
            temp=novoEstado[4]
            novoEstado[4]=novoEstado[5]
            novoEstado[5]=temp
        return novoEstado
    if(index==5):
        if(direcao==1):
            temp=novoEstado[5]
            novoEstado[5]=novoEstado[2]
            novoEstado[2]=temp
        if(direcao==2):
            temp=novoEstado[5]
            novoEstado[5]=novoEstado[8]
            novoEstado[8]=temp
        if(direcao==3):
            temp=novoEstado[5]
            novoEstado[5]=novoEstado[4]
            novoEstado[4]=temp
        if(direcao==4):
            return None
        return novoEstado
    if(index==6):
        if(direcao==1):
            temp=novoEstado[6]
            novoEstado[6]=novoEstado[3]
            novoEstado[3]=temp
        if(direcao==2):
            return None
        if(direcao==3):
            return None
        if(direcao==4):
            temp=novoEstado[6]
            novoEstado[6]=novoEstado[7]
            novoEstado[7]=temp
        return novoEstado
    if(index==7):
        if(direcao==1):
            temp=novoEstado[7]
            novoEstado[7]=novoEstado[4]
            novoEstado[4]=temp
        if(direcao==2):
            return None
        if(direcao==3):
            temp=novoEstado[7]
            novoEstado[7]=novoEstado[6]
            novoEstado[6]=temp
        if(direcao==4):
            temp=novoEstado[7]
            novoEstado[7]=novoEstado[8]
            novoEstado[8]=temp
        return novoEstado
    if(index==8):
        if(direcao==1):
            temp=novoEstado[8]
            novoEstado[8]=novoEstado[5]
            novoEstado[5]=temp
        if(direcao==2):
            return None
        if(direcao==3):
            temp=novoEstado[8]
            novoEstado[8]=novoEstado[7]
            novoEstado[7]=temp
        if(direcao==4):
            return None
        return novoEstado
    
def main():

    global GoalNode

    parser = argparse.ArgumentParser()
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")

    InitialState = []
    InitialState.append(int(data[0]))
    InitialState.append(int(data[1]))
    InitialState.append(int(data[2]))
    InitialState.append(int(data[3]))
    InitialState.append(int(data[4]))
    InitialState.append(int(data[5]))
    InitialState.append(int(data[6]))
    InitialState.append(int(data[7]))
    InitialState.append(int(data[8]))

    bfs(InitialState)

    movimentos = []

    while InitialState != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Up'
        if GoalNode.move == 2:
            path = 'Down'
        if GoalNode.move == 3:
            path = 'Left'
        if GoalNode.move == 4:
            path = 'Right'
        movimentos.insert(0, path)
        GoalNode = GoalNode.parent

    print(movimentos)
    print(len(movimentos))
    


if __name__ == '__main__':
    main()