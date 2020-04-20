import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import random 
import matplotlib.animation as animation 

darts=10000
dframes=100# dumping inverval of frames  
duration=10  #sec 

nDartInsideCircle=0  
nThrowns=0  


ims=[]
fig = plt.figure(figsize=(12,5))
ax1=fig.add_axes([0.05,0.12,0.40,0.8])
ax2=fig.add_axes([0.51,0.12,.45,0.8])
ax2.axhline(y=3.1416,linewidth=1,color='r')

ax1.get_xaxis().set_tick_params(which='both',direction='inout')
ax2.get_xaxis().set_tick_params(which='both',direction='inout')
ax1.get_yaxis().set_tick_params(which='both',direction='inout')
ax2.get_yaxis().set_tick_params(which='both',direction='inout')


ax1.xaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax1.xaxis.set_major_locator(plt.MultipleLocator(0.50))
ax1.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax1.yaxis.set_major_locator(plt.MultipleLocator(0.50))

ax1.set_aspect('equal', 'box') 
ax1.set_xlim(-1,1) 
ax1.set_ylim(-1,1) 

ax2.set_xlim(0,darts)
ax2.set_ylim(2.85,3.45) 

ax1.set_xlabel(r'$x$',size=20)
ax1.set_ylabel(r'$y$',size=20) 

ax2.set_xlabel(r'$\mathrm{Darts}$')
ax2.set_ylabel(r'$\mathrm{\pi}$',size=25) 

ax1.add_artist(plt.Circle((0, 0), 1.0,color='black',fill=False)) 


pt=[]
pi=[]


x_in=[]
y_in=[]
x_out=[] 
y_out=[] 


props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
ax2.text(darts/3.1,3.35,
    r'$\pi=4\frac{\mathrm{Red\; Darts}}{\mathrm{Total\;Darts}}$' 
    ,color='#8e3463',fontsize=25)
nframes=0 
for i in range(darts): 
    randX=2*random.random()-1.0
    randY=2*random.random()-1.0 
    
    if ((randX*randX + randY*randY) < 1): 
        nDartInsideCircle+=1  
        x_in.append(randX)
        y_in.append(randY) 
    else: 
        x_out.append(randX)
        y_out.append(randY) 
   
    if (i%dframes==0): 
        nframes+=1 
        ipi=4*(nDartInsideCircle/float(i+1))
        print(i+1,ipi) 
        pt.append(i+1)
        pi.append(ipi)
        pi_plot=ax2.scatter(pt,pi,color='b',marker='o',s=3)
        last_point=ax2.scatter(pt[-1],pi[-1],color='r',marker='o',s=20)
        circle1=ax1.scatter(x_in,y_in,color='r',s=3)
        circle2=ax1.scatter(x_out,y_out,color='g',s=3)
        
        txt1=ax2.text(darts/1.7,2.95,r'$\pi=\;$'+'%.6f'%(ipi),bbox=props)
        txt2=ax2.text(darts/10,2.95,r'$\mathrm{Darts=}\;$'+'%d'%(i),bbox=props)
        ims.append([circle1,circle2,pi_plot,last_point,txt1,txt2])


fps=nframes/duration
interval=(duration*1000)/nframes  

ani = animation.ArtistAnimation(fig,ims,interval=interval)
ani.save('pi.mp4',fps=fps, dpi=100)
ani.save('pi.gif', dpi=100,writer='imagemagick')

plt.show() 
