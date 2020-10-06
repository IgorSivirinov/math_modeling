ear = int(input('Год: '))
if (ear%4==0 and ear%100!=0) or (ear%400==0 and ear%100==0):
    print(ear, 'высокостный')
else:
    print(ear, 'не высокостный')

