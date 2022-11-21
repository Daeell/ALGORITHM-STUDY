#키 로거
import sys
from collections import deque
input=sys.stdin.readline

N=int(input().strip())

for _ in range(N):
    A=[]
    A=list(input().strip())
    cnt = 0
    answer=deque()
    for i in A:
        if answer != None:
            if i == '<':
                if len(answer)==0 or cnt ==0:
                    cnt=0
                else:
                    cnt -=1
            elif i ==">":
                cnt +=1
                if len(answer)+cnt>=len(answer) or len(answer) ==0:
                    cnt=0
            elif i == "-":
                if len(answer)+cnt<0:
                    continue
                elif len(answer)+cnt>len(answer):
                    answer.pop()
                else:
                    del answer[len(answer)+cnt]
            else:
                answer.insert(len(answer)+cnt,i)
    print(*answer,sep='')

