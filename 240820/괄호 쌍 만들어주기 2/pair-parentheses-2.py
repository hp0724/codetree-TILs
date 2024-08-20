input_value = input()
cnt = 0 
for i in range(len(input_value)-2):
    for j in range(i+1,len(input_value)-1):
        if input_value[i] == "(" and input_value[i+1] =="(" and input_value[j] == ")" and input_value[j+1]== ")":
            cnt += 1 

print(cnt)