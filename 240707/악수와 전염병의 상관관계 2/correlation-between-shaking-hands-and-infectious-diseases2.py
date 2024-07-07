# N명의 개발자들이 있으며, T번에 걸쳐 t초에 x개발자가 y개발자와 악수를 나눈 정황이 주어집니다. 
# 전염된 x 개발자와 전염된 y 개발자끼리 악수를 해도 전염병을 옮기게 되는 횟수 포함
# N 개발자 수 
# K번의 악수 동안만 전염병을 옮기게 되고
# 처음 전염병에 걸려 있는 개발자의 번호 P
N,K,P,T = map(int,input().split())

N_arr = [0]*(N+1)
N_handshake_cnt_arr = [K]*(N+1)

N_arr[P] = 1

#  t초에 x 개발자와 y 개발자가 악수를 나눴음을 의미
handshake_arr = []
for _ in range(T):
    t,x,y = map(int,input().split())
    handshake_arr.append((t,x,y))

handshake_arr.sort()
for t,x,y in handshake_arr:
    if N_arr[x] == 1 and N_handshake_cnt_arr[x]!=0:
        N_arr[y] = 1 
        N_handshake_cnt_arr[x] -= 1 
    elif N_arr[y] == 1 and N_handshake_cnt_arr[y]!=0:
        N_arr[x] = 1 
        N_handshake_cnt_arr[y] -=1

N_arr = N_arr[1:]
print("".join(map(str,N_arr)))