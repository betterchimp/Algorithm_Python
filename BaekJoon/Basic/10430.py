'''
첫째 줄에 (A+B)%C, 
둘째 줄에 ((A%C) + 
(B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
'''

def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    
    print((A+B)%C)
    print(((A%C)+(B%C))%C)
    print((A*B)%C)
    print(((A%C)*(B%C))%C)

main()