f = open('26-peps2.txt')
k,s,summ = map(int, f.readline().split())
d =[]
for i in range(k):
    a, b, c = f.readline().split()
    d.append([a, b, c])
    
d.sort(key= lambda x: x[1])
mas1 = []
mas2 = []
for i in range(k):
    if d[i][1] == 'B':
        mas1.append([d[i][0], d[i][2]])
    else:
        mas2.append([d[i][0], d[i][2]])

masr1 = []
masr2 = []
for i in range(len(mas1)):
    if mas1[i][0] == 'D':
        masr1.append([mas1[i][0], int(mas1[i][1]) * 0.7+summ])
    else:
        masr1.append([mas1[i][0], int(mas1[i][1])])
     
for i in range(len(mas2)):
    if mas2[i][0] == 'D':
        masr2.append([mas2[i][0], int(mas2[i][1]) * 0.7+summ])
    else:
        masr2.append([mas2[i][0], int(mas2[i][1])])
        
masr1.sort(key = lambda x: x[1])        
masr2.sort(key = lambda x: x[1])
summ1 = masr1[0][1]
k1 = 1
maxxk1 = 0
maxxs1 = 0
for i in range(1,len(masr1)):
    if summ1 + masr1[i][1] <= s:
        k1 += 1
        summ1 += masr1[i][1]
        maxxk1 = max(k1, maxxk1)
        maxxs1 = max(summ1, maxxs1)
    else:
        break

summ2 = masr2[0][1]
k2 = 1
maxxk2 = 0
maxxs2 = 0
maxxres2 = 0
for i in range(1,len(masr2)):
    if summ2 + masr2[i][1] <= s:
        k2 += 1
        summ2 += masr2[i][1]
        maxxk2 = max(k2, maxxk2)
        maxxs2 = max(summ2, maxxs2)
        if masr2[i][0] =='D':
            maxxres2 = max(masr2[i][1], maxxres2)
    else:
        break

ostatok_money_proigravshiy = s - maxxs2 + maxxres2
maxx_res_proigravshiy = 0
for i in range(len(masr2)):
    if masr2[i][0] =='D' and masr2[i][1] < ostatok_money_proigravshiy:
        maxx_res_proigravshiy = max(maxx_res_proigravshiy, masr2[i][1])
               
print('Всего машин у победителя:', maxxk1 + maxxk2)
print()
print('Максимальная стоимость дефектного авто у проигравшего:', int(maxx_res_proigravshiy))

    





        
               


