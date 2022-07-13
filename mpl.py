import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter  import *




okno = Tk()
okno.title('Модель идеального газа')
okno.geometry('480x270+500+200')

l_r = Label(okno, text = "Введите радиус молекул:")
l_r.place(x = 5, y = 5, height = 15, width = 150)

e_r = Entry(okno, bg="darkgreen")
e_r.place(x = 160, y = 5, height = 20, width = 50)

l_N = Label(okno, text = "Введите число молекул:")
l_N.place(x = 5, y = 35, height = 15, width = 150)

e_N = Entry(okno, bg="darkgreen")
e_N.place(x = 160, y = 35, height = 20, width = 50)


def start():
    global r, N, x, y, vx, vy
    r = float(e_r.get())    
    N = int(e_N.get())
    

    t = 0.05
    x = np.random.rand(N)*10-5 #[-5, 5]
    y = np.random.rand(N)*10-5
    l = []

    vx = np.random.rand(N)-0.5  #[-0.5, 0.5] 
    vy = np.random.rand(N)-0.5


    def P(i,j):
        return ((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2)

    # функция рассчитывает скорости шаров после удара
    def yd(i,j):    # 1 шар: i, v;      2 шар: j, u.     Индекс v1 - до удара, v2 - после удара
        global x,y,vx,vy
        k = [x[j] - x[i], y[j]-x[i]]
        mod_k = (k[0]**2 + k[1]**2 )**(1/2)
        k[0] = k[0]/mod_k
        k[1] = k[1]/mod_k
        k = np.array(k)
        #------------------- создали k - masiv numpy
        f = [0,0]
        f[0] = -abs(k[0])*k[1]/k[0]
        f[1]= abs(k[0])
        f = np.array(f)
        #------------------- создали f
        v1 = np.array(  [vx[i],vy[i]]  )
        u1 = np.array(  [vx[j],vy[j]]  )
        v2_f = np.dot(v1,f)*f
        u2_f = np.dot(u1,f)*f
        v1_k = np.dot(v1,k)
        u1_k = np.dot(u1,k) # - это проекция 
        #------------------- создали v2_f и v2_f , v1_k и u1_k
        v2_k = u1_k*k
        u2_k = v1_k*k
        #------------------- было просто
        v2 = v2_f + v2_k
        u2 = u2_f + u2_k
        return np.stack((v2,u2))

    # функция для подсчёта импульса системыы m = 1
    def imp():
        global vx , vy
        s = 0
        S = 0
        for i in range(N):
            s = s + vx[i] + vy[i]
            S = S + vx[i]**2 + vy[i]**2
        return [s,S]
    #--------------------------------
    fig, ax = plt.subplots()
    ln = plt.plot([],[], 'ro')[0]


    def init():
        ax.set_xlim(-6,6)
        ax.set_ylim(-6, 6)
        
        return (ln,)

    def update(frame):
        global x, y, vx,vy

        for i in range(N):
            if abs(x[i]) >= 6:
                vx[i] *= -1
                
            if abs(y[i]) >= 6:
                vy[i] *= -1
                
        
        for i in range(N):
            for j in range(i+1, N):
                rast = P(i,j)
                v = (i,j)
                if rast <= 2*r and v not in l :
                    l.append((i,j))
                    z = yd(i,j)
                    vx[i] = z[0][0]
                    vy[i] = z[0][1]
                    vx[j] = z[1][0]
                    vy[j] = z[1][1]
                    
                    
                if rast >2*r and v in l:
                    l.remove(v)
            #cc = plt.Circle((x[i],y[i]),r)            
            #ax.add_artist(cc)
        x += vx*frame
        y += vy*frame
        ln.set_data(x, y)
        
        
        
        return (ln,)

    ani = FuncAnimation(fig, update, frames=[t],
                        init_func=init, blit=True, interval = 1) # в милисекундах
    plt.show()



    

b = Button(okno, text = "Запуск", command = start)
b.place(x = 220, y = 5, height = 50, width = 100)

okno.mainloop()















