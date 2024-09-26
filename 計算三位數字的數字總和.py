n = input('請輸⼊⼀個三位數：')

s = 0

for i in range(len(n)):
    s += int(n[i])
    
print(f'每位數字的總和：{s}')