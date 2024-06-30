def hello_world(n):
    if n == 0:
        return 
    print("HelloWorld")
    hello_world(n-1)

hello_world(4)