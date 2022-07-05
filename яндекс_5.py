N = int(input())
svazi = {}

#--------------------реализация функции, отороя ищет путь между точками графа
def poisk(otkyda, kyda): # если она нашла, то изменяет глобальную переменную resolt
    bil.append(otkyda)
    #print('я в {}, мне в {}'.format(otkyda, kyda) ) #для контроля выполнения
    #print('bil = ',bil)     #для контроля выполнения
    global resolt
    if resolt >= 1:  # очистка стека вызова после нахождения
        return 0
    way = svazi.get(otkyda).copy()
    for i in bil:
        if i in way:
            way.remove(i)  #чтобы не идти туда, где был
    #print('way = ',way)
    if len(way) == 0:  #тупик
        return 0
    if kyda in way:  # нашли
        resolt += 1
        return 0
    else:
        for i in way:
            poisk(i,kyda) # любимая рекурсия
    

#--------------------функция для создания словаря svazi
def add_svaz(ind):  #ind = [ind_1 , ind_2]
    ind_1 = ind[0]
    ind_2 = ind[1]
    Bool_1 = ind_1 in svazi.keys()
    Bool_2 = ind_2 in svazi.keys()
    if Bool_1:
        if ind_2 not in svazi[ind[0]]:
             svazi[ind_1].append(ind_2)
    if not Bool_1:
        svazi.setdefault(ind_1,[ind_2])

    if Bool_2:
        if ind_1 not in svazi[ind_2]:
             svazi[ind_2].append(ind_1)
    if not Bool_2:
        svazi.setdefault(ind_2,[ind_1])
    #print(svazi)

#инициализация svazi
for i in range(N):
    add_svaz(input().split())

T = int(input())
zapr = []  # zapr = [[zapr_1], [zapr_2] ... ], zapr_i = [kyda, N, otkyda_1,..., otkyda_N]

#инициализация списка запросов
for i in range(T):
    a = []
    for i in input().split():
        a.append(i)
    for i in input().split():
        a.append(i)
    zapr.append(a)

# ответы по запросам
for zapr_i in zapr:
    kyda = zapr_i[0]
    otvet = ''
    n = 0
    for otkyda_i in zapr_i[2:]:
        bil = [] # при поиске необходимо знать где я был
        resolt = 0 
        poisk(otkyda_i,kyda)
        if resolt >= 1:
            n += 1
            otvet += otkyda_i + " "
    print(str(n)+ " " + otvet)


