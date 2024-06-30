def hello_world(n):
    if n == 0:
        return 
    print("HelloWorld")
    hello_world(n-1)

n = int(input())
hello_world(n)