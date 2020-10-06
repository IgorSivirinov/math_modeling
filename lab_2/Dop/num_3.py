s = input('Ввидите число: ')
t = ''
for ch in range(len(s)-1,-1,-1):
    t += s[ch]
print(t)