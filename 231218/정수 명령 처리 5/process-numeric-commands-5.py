n=input()
result=[]
for _ in range(int(n)):
    command=input().split()
    if command[0]=="push_back":
        result.append(int(command[1]))
    elif command[0] =="get":
        print(result[int(command[1])-1])
    elif command[0] == "size":
        print(len(result))
    elif command[0] == "pop_back":
        result.pop()