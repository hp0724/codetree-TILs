import sys 
input = sys.stdin.readline
binary = input()
binary = list(map(int,binary))
num = 0
for i in range(len(binary)):
    num = num *2 + binary[i]

print(num)