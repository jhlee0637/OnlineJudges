# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
#
# 위 문제는 '큐'를 활용하여 풀 수 있는 문제다.
# 따라서 데이터 구조론에서 배운 내용에 맞춰 class를 통해 'equeue', 'dequeue' 기능을 구현해서 풀어봤다.
# While문 대신 recursive를 사용해봤다.
#
# Python의 경우 recursion을 999회로 제한해놨기 때문에, 프로그래머스 테스트 케이스에서 999회 이상의 recursive가 발생하는 경우에는 런타임에러가 발생했다.
# Python의 resursion을 999회 이상으로 설정하는 방법은 다음과 같다.
#   import sys
#   sys.setrecursionlimit(숫자)
#
# recursion을 적용해보겠다는 생각은 좋았지만, 시간이나 효율이 좋지 않았다.
# 한 테스트 케이스에서는 시간초과가 발생해서 결국 아래의 코드는 문제를 푸는데는 적합하지 않았다.


class Bridge:
    limitWeight=0
    limitLength=0
    def __init__(self, length, totalWeight, time):
        self.length=length
        self.totalWeight=totalWeight
        self.time=time

    def addTruck(self, newWeight): # enqueue, FIFO
        self.totalWeight+=newWeight
        self.length+=[newWeight]

    def rmTruck(self): # dequeue, FIFO
        out_truck=self.length[0]
        self.totalWeight-=out_truck
        self.length.pop(0)

def simulateBridge(bridge, new_weight):
    bridge.rmTruck()
    bfrWeight=bridge.totalWeight
    aftWeight=bfrWeight+new_weight
    bfrLength=bridge.length
    aftLength=bfrLength+[new_weight]
    if aftWeight>bridge.limitWeight or len(aftLength)>bridge.limitLength:
        bridge.time+=1
        bridge.addTruck(0)
        simulateBridge(bridge, new_weight) #recursive
    else:
        bridge.time+=1
        bridge.addTruck(new_weight)
    return bridge

def solution(bridge_length, weight, truck_weights):
    bridgelength=[0]*bridge_length
    Bridge.limitWeight=weight
    Bridge.limitLength=bridge_length
    # first truck
    f_truck=truck_weights[0]
    solBridge=Bridge(bridgelength, f_truck, 1)
    solBridge.length[-1]=f_truck
    # rest truck
    for w in truck_weights[1:400]:
        solBridge=simulateBridge(solBridge, w)
    solBridge.time+=bridge_length
    answer=solBridge.time
    return answer

# 다음은 데이터구조 강의를 듣기 전에 클래스를 사용하지 않고 모든 테스트 케이스를 통과하게 풀었던 답변이다.
'''
def solution(bridge_length, weight, truck_weights):
    int_TruckLimit      = bridge_length
    int_WeightLimit     = weight
    li_TruckWaiting     = truck_weights
    li_TruckOnBridge    = [0]*(int_TruckLimit)
    time=0
    
    for truck in li_TruckWaiting:
        
        time+=1
        del li_TruckOnBridge[0]
        li_TruckOnBridge += [truck]
        
        int_WeightOnBridge = sum(li_TruckOnBridge)
        
        if int_WeightOnBridge > int_WeightLimit:
            while int_WeightOnBridge > int_WeightLimit:
                int_WeightOnBridge = int_WeightOnBridge - li_TruckOnBridge[0]
                
                del li_TruckOnBridge[-1]
                li_TruckOnBridge +=[0]
                
                time+=1
                del li_TruckOnBridge[0]
                li_TruckOnBridge += [truck]

    time += int_TruckLimit
        
    answer=time
    return answer
'''