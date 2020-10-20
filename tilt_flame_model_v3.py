#倾斜圆柱火焰模型
import traceback

from sympy import Symbol, sqrt, cos, sin, atan, log, nsolve, solveset,solve
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np
import math
# from scipy.interpolate import make_interp_spline
import   matplotlib.backends.backend_tkagg





pi=np.pi
# #R=15
#
# X=50
# H=20
# theta=45/180*pi
# #a=H/R
# #b=X/R
# #火焰发射率数据epsilon range(0~1),T=火焰温度
# epsilon=0.5 发射率直接设置
# epsilon=1-math.e**(k*np.max(d_flame)) #发射率通过k进行计算，d_flame是所有的直径，最大值是倾斜火焰直径，如果你算出的火焰形态的d_flame就是最大值,那就是epsilon=1-math.e**(k*d_flame)
sigma=5.67*(10**(-8))
# T=400 #tempreture
# E=epsilon*sigma*(T**4)



def close_handle(evt):
    global  closed
    closed = True
    print("close")




#6.1 当观察者位于火焰倾斜方向的位置时，其视角系数
#6.1.1垂直视角系数
# def FV1_func(H, X, theta, X):
#     a=H/R
#     b=X/R

def FV1_func(fireHeight, fireWidth, theta, R_distance ):
    H = fireHeight / (cos(theta))
    a = H / fireWidth
    b = R_distance / fireWidth
    if b==1 or b==-1:
        b=b+0.0001
    theta=theta/180*pi
    fv_val=-a*cos(theta)/(pi*(b-a*sin(theta)))*atan(sqrt((b-1)/(b+1)))+a*cos(theta)/(pi*(b-a*sin(theta)))\
    *(a**2+(b+1)**2-2*b*(1+a*sin(theta)))/(sqrt(a**2+(b+1)**2-2*a*(b+1)*sin(theta))*sqrt(a**2+(b-1)**2-2*a*(b-1)*sin(theta)))\
    *atan(sqrt((a**2+(b+1)**2-2*a*(b+1)*sin(theta))/(a**2+(b-1)**2-2*a*(b-1)*sin(theta)))*sqrt((b-1)/(b+1)))+cos(theta)/(pi*sqrt(1+(b**2-1)*cos(theta)**2))\
    *((atan((a*b-(b**2-1)*sin(theta))/(sqrt(b**2-1)*sqrt(1+(b**2-1)*cos(theta)**2))))+(atan(((b**2-1)*sin(theta))/(sqrt(b**2-1)*sqrt(1+(b**2-1)*cos(theta)**2)))))
    return fv_val

#6.1.2水平视角系数
#6.1.2水平视角系数计算函数
def FH1_func(fireHeight, fireWidth, theta, R_distance):

    H = fireHeight / (cos(theta))
    a=H/fireWidth
    b=R_distance/fireWidth
    if b==1 or b==-1:
        b=b+0.0001
    theta=theta/180*pi
    x1=a**2+(b+1)**2-2*a*(b+1)*sin(theta)
    x2=a**2+(b-1)*(b-1)-2*a*(b-1)*sin(theta)
    fh_val=atan(pow(((b+1)/(b-1)),0.5))/pi+sin(theta)/(pi*pow(1+(b**2-1)*cos(theta)*cos(theta),0.5))\
           *((atan((a*b-(b**2-1)*sin(theta))/(pow((b**2-1),0.5)*pow((1+(b**2-1)*cos(theta)*cos(theta)),0.5))))+(atan(((b**2-1)*sin(theta))/(pow((b**2-1),0.5)*pow((1+(b**2-1)*cos(theta)*cos(theta)),0.5)))))\
           -(a**2+(b+1)**2-2*(b+1+a*b*sin(theta)))/(pi*(pow(x1,0.5)*pow(x2,0.5)))\
           *atan(pow(((a**2+(b+1)**2-2*a*(b+1)*sin(theta))/(a**2+(b-1)*(b-1)-2*a*(b-1)*sin(theta))),0.5)*pow(((b-1)/(b+1)),0.5))
    return fh_val

#6.2当观察者位于垂直于火焰倾斜方向的位置时，其视角系数
#6.2.1水平视角系数：
def FH2_func(fireHeight, fireWidth, theta, R_distance):
    H = fireHeight / (cos(theta))
    a = H / fireWidth
    b = R_distance / fireWidth
    if b==1 or b==-1:
        b=b+0.0001
    fh2_val=atan(pow(((b-1)/(b+1)),0.5))/pi+pow((b**2-1),0.5)*sin(theta)/(2*pi*pow(b**2-sin(theta)*sin(theta),0.5))\
        *(atan((a*b/pow(b**2-1,0.5)+sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5)))-atan((a*b/pow(b**2-1,0.5)-sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5)))-2*atan(sin(theta)/pow((b**2-sin(theta)*sin(theta)),0.5)))\
        -(a**2+b**2-1)/(2*pi*pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5))\
        *(atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)-2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5)))+atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)+2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5))))
    return fh2_val

#6.2.2垂直视角系数：
def FV2_func(fireHeight, fireWidth, theta, R_distance):
    H = fireHeight / (cos(theta))
    a = H / fireWidth
    b = R_distance / fireWidth
    if b==1 or b==-1:
        b=b+0.0001
    theta=theta/180*pi
    fv2_val=-(a**2*sin(theta)*cos(theta)/(4*pi*(b**2+a**2*sin(theta)*sin(theta))))*log((a**2+b**2-1-2*a*pow((b**2-1),0.5)*sin(theta)/b)/(a**2+b**2-1+2*a*pow((b**2-1),0.5)*sin(theta)/b))+cos(theta)/(2*pi*pow((b**2-sin(theta)*sin(theta)),0.5))\
        *(atan((a*b/pow(b**2-1,0.5)+sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5)))+atan((a*b/pow(b**2-1,0.5)-sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5))))-a*b*cos(theta)/(pi*(b**2+a**2*sin(theta)*sin(theta)))\
        *atan(pow(((b-1)/(b+1)),0.5))+(a*b*cos(theta)*(a**2+b**2+1))/(2*pi*(b**2+a**2*sin(theta)*sin(theta))*pow((pow(a**2+b**2+1,2)-4*(b**2+a**2*sin(theta)*sin(theta))),0.5))\
        *(atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)-2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5)))+atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)+2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5))))
    return fv2_val
##############水平热流密度#################################
#Radiative heat flux curve
#水平热流密度，沿火焰倾斜方向
def draw_rad_heat_flux_curve_FH1_x_pos(H, W, theta, epsilon, T, R_distance, fig):
    try:
        plt.clf()
        plt.ion()
        x = np.arange(1, R_distance, 1) #Radius
        y = []
        E=epsilon*sigma*(T**4)
        for x_dis in x:
            y_1 = FH1_func(H, W, theta, x_dis)*E
            y.append(abs(y_1))
        plt.plot(x, y, label="Horizontal radiative heat flux (along the tilt flame)")
        plt.xlabel("Distance to flame (m)")
        plt.ylabel("Radiative heat flux (kW/m^2)")
        plt.legend()
        plt.pause(1)
        plt.show()
    except Exception as e:
        print(e)

#水平热流密度，背向火焰倾斜方向
def draw_rad_heat_flux_curve_FH1_x_neg(H, W,theta,epsilon, T, R_distance, fig):
    try:
        plt.ion()
        plt.clf()
        x = np.arange(R_distance*(-1), 0, 1) #Radius
        y = []
        E=epsilon*sigma*(T**4)
        for x_dis in x:
            y_1 = FH1_func(H, W, theta, x_dis)*E
            y.append(abs(y_1))
        plt.plot(x, y, label="Horizontal radiative heat flux (back to the tilt flame)")
        plt.xlabel("Distance to flame (m)")
        plt.ylabel("Radiative heat flux (kW/m^2)")
        plt.legend()
        plt.pause(1)
        plt.show()
    except Exception as e:
        print(e)
#当观察者位于垂直于火焰倾斜方向的位置时，视角系数为FH2
#水平热流密度，垂直火焰倾斜方向
def draw_rad_heat_flux_curve_FH2_y_vertical(H, W,theta,epsilon, T, R_distance, fig):
    try:
        plt.clf()
        plt.ion()
        x = np.arange(1, R_distance, 1) #Radius
        y = []
        E=epsilon*sigma*(T**4)
        for x_dis in x:
            y_1 = FH2_func(H, W, theta, x_dis)*E
            y.append(abs(y_1))
        plt.plot(x, y, label="Horizontal radiative heat flux (perpendicular to the tilt flame)")
        plt.xlabel("Distance to flame (m)")
        plt.ylabel("Radiative heat flux (kW/m^2)")
        plt.legend()
        plt.pause(1)
        plt.show()
    except Exception as e:
        print(e)
##############水平热流密度#################################



##############垂直热流密度#################################
#Radiative heat flux curve
#垂直热流密度，沿火焰倾斜方向
def draw_rad_heat_flux_curve_FV1_x_pos(H, W,theta,epsilon, T, R_distance, fig):
    plt.ion()
    plt.clf()
    x = np.arange(1, R_distance, 1) #Radius
    y = []
    E = epsilon * sigma * (T ** 4)
    for x_dis in x:
        y_1 = FV1_func(H, W, theta, x_dis)*E
        y.append(abs(y_1))
    plt.plot(x, y, label="Vertical radiative heat flux (along the tilt flame)")
    plt.xlabel("Distance to flame (m)")
    plt.ylabel("Radiative heat flux (kW/m^2)")
    plt.legend()
    plt.pause(1)
    plt.show()
#垂直热流密度，背向火焰倾斜方向
def draw_rad_heat_flux_curve_FV1_x_neg(H, W,theta,epsilon, T, R_distance, fig):
    plt.ion()
    plt.clf()
    x = np.arange(R_distance*(-1), 0, 1) #Radius
    y = []
    E = epsilon * sigma * (T ** 4)
    for x_dis in x:
        y_1 = FV1_func(H, W, theta, x_dis)*E
        y.append(abs(y_1))
    plt.plot(x, y, label="Vertical radiative heat flux (back to the tilt flame)")
    plt.xlabel("Distance to flame (m)")
    plt.ylabel("Radiative heat flux (kW/m^2)")
    plt.legend()
    plt.pause(0.1)
    plt.show()
#当观察者位于垂直于火焰倾斜方向的位置时，视角系数为FH2
#垂直热流密度，垂直火焰倾斜方向
def draw_rad_heat_flux_curve_FV2_y_vertical(H, W,theta,epsilon, T, R_distance, fig):
    plt.ion()
    plt.clf()
    x = np.arange(0, R_distance, 1) #Radius
    y = []
    E = epsilon * sigma * (T ** 4)
    for x_dis in x:
        y_1 = FV2_func(H, W, theta, x_dis)*E
        y.append(abs(y_1))
    plt.plot(x, y, label="Vertical radiative heat flux (perpendicular to the tilt flame)")
    plt.xlabel("Distance to flame (m)")
    plt.ylabel("Radiative heat flux (kW/m^2)")
    plt.legend()
    plt.pause(1)
    plt.show()
##############垂直热流密度#################################

# 给定辐射热流rad_heat时，a点位置的计算函数
def tilt_flame_rad_heat_pa(H, R, theta, epsilon, T,  rad_heat):
    try:
        X_a = Symbol('X_a')
        #rad_heat=rad_heat
        #Example:
        #H=20
        #X=50
        theta=theta/180*pi
        a=H/R
        #b=X/R
        b=X_a/R
        E=epsilon*sigma*(T**4)
        x1=a**2+(b+1)**2-2*a*(b+1)*sin(theta)
        x2=a**2+(b-1)*(b-1)-2*a*(b-1)*sin(theta)
        FH1=atan(pow(((b+1)/(b-1)),0.5))/pi+sin(theta)/(pi*pow(1+(b**2-1)*cos(theta)*cos(theta),0.5))\
            *((atan((a*b-(b**2-1)*sin(theta))/(pow((b**2-1),0.5)*pow((1+(b**2-1)*cos(theta)*cos(theta)),0.5))))+(atan(((b**2-1)*sin(theta))/(pow((b**2-1),0.5)*pow((1+(b**2-1)*cos(theta)*cos(theta)),0.5)))))\
            -(a**2+(b+1)**2-2*(b+1+a*b*sin(theta)))/(pi*(pow(x1,0.5)*pow(x2,0.5)))\
            *atan(pow(((a**2+(b+1)**2-2*a*(b+1)*sin(theta))/(a**2+(b-1)*(b-1)-2*a*(b-1)*sin(theta))),0.5)*pow(((b-1)/(b+1)),0.5))
        #This is for test:f_qv_r0=FV1-0.118
        func_qh_xa=FH1*E-rad_heat
        result=nsolve(func_qh_xa, X_a, R+0.3) # 20 is the initial guess, this is required for nsolve function
        X_a=result
        #this is the Hazardous Radius (5 values)
        # print(X_a)
        return(X_a)
    except Exception as e:
        traceback.print_exc()
        return 0

def tilt_flame_hazardous_radius_xa(H, R, theta, epsilon, T, rad_heat, fig):
    try:
        plt.ion()
        # rad_heat=[1.6,4.0,12.5,25.0,30.0]
        R_5=[0,0,0,0,0]

        for i in range(5):
            try:
                R_5[i]=tilt_flame_rad_heat_pa(H, R, theta, epsilon, T, rad_heat[i])
                # print(R_5[i])
            except:
                traceback.print_exc()
        #this is the Hazardous Radius (5 values)
        #plot the hazardous radius
        # fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111)
        colors = ["orange","cyan","pink","lime","yellow"]
        for i in range(5):
            try:
                cir = Circle(xy = (0.0, 0.0), radius=R_5[i], facecolor= colors[i]) #alpha=0.5,
                ax.add_patch(cir)
                x, y = 0, 0
                ax.plot(x, y, 'ro')
                #step=max(R_5)/15.0
                # plt.text(0.0, 0.1*i, 'R'+str(5-i)+'='+str(round(R_5[i],3)), ha='right', wrap=True, rotation='horizontal')
                plt.title('Hazardous Radius (5 levels)')
                plt.axis('scaled')
                plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
            except:
                continue
        plt.pause(2)
        plt.show()
    except Exception as e:
        traceback.print_exc()
        plt.pause(3)

def tilt_flame_hazardous_radius_xb(H, R, theta, epsilon, T,rad_heat, fig):
    try:
        # fig.canvas.mpl_connect('close_event', lambda evt:fig.close())

        plt.ion()
        # rad_heat=[1.6,4.0,12.5,25.0,30]
        R_5=[0,0,0,0,0]
        for i in range(5):
            try:
                R_5[i]=tilt_flame_rad_heat_pb(H, R, theta, epsilon, T, rad_heat[i])
            except :
                continue
        #this is the Hazardous Radius (5 values)
        #plot the hazardous radius
        # fig = plt.figure()
        plt.clf()

        ax = fig.add_subplot(111)
        colors = ["orange","cyan","pink","lime","yellow"]
        for i in range(5):
            try:
                cir = Circle(xy = (0.0, 0.0), radius=R_5[i], facecolor= colors[i]) #alpha=0.5,
                ax.add_patch(cir)
                x, y = 0, 0
                ax.plot(x, y, 'ro')
                #ax.arrow(0,0,int(R_5[i]),i*10,length_includes_head = True, head_width = 2, head_length = 2,fc = 'k',ec = 'k')
                #plt.text(int(R_5[i]), i*10, str(round(R_5[i],3)), ha='right', wrap=True, rotation='vertical')
                # plt.text(0.0,0.1*i, 'R'+str(5-i)+'='+str(round(R_5[i],3)), ha='right', wrap=True, rotation='horizontal')
                plt.title('Hazardous Radius (5 levels)')
                plt.axis('scaled')
                plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
            except :
                continue
        plt.pause(2)

        plt.show()
    except Exception as e:
        traceback.print_exc()
        plt.pause(3)


def tilt_flame_hazardous_radius_xc(H, R, theta, epsilon, T, rad_heat, fig):
    try:
        plt.ion()
        # rad_heat=[1.6,4.0,12.5,25.0,30.0]
        R_5=[0,0,0,0,0]

        for i in range(5):
            try:
                R_5[i]=tilt_flame_rad_heat_pc(H, R, theta, epsilon, T, rad_heat[i])
            except Exception as e:
                continue
        #this is the Hazardous Radius (5 values)
        #plot the hazardous radius
        # fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111)
        colors = ["orange","cyan","pink","lime","yellow"]
        for i in range(5):
            try:
                cir = Circle(xy = (0.0, 0.0), radius=R_5[i], facecolor= colors[i]) #alpha=0.5,
                ax.add_patch(cir)
                x, y = 0, 0
                ax.plot(x, y, 'ro')
                #ax.arrow(0,0,int(R_5[i]),i*10,length_includes_head = True, head_width = 2, head_length = 2,fc = 'k',ec = 'k')
                #plt.text(R_5[i], 0, str(round(R_5[i],3)), ha='right', wrap=True, rotation='vertical')
                #step=max(R_5)/5
                plt.text(0.0, 1*i, 'R'+str(5-i)+'='+str(round(R_5[i],3)), ha='right', wrap=True, rotation='horizontal')
                plt.title('Hazardous Radius (5 levels)')
                plt.axis('scaled')
                plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
            except Exception as e:
                continue
        plt.pause(3)
        plt.show()
    except Exception as e:
        traceback.print_exc()
        plt.pause(3)

# 给定辐射热流rad_heat时，b点位置的计算函数（x轴负半轴位置）
def tilt_flame_rad_heat_pb(H, R, theta, epsilon, T, rad_heat):
    return tilt_flame_rad_heat_pa(H, R, 180-theta, epsilon, T, rad_heat)

# 给定辐射热流rad_heat时，c点位置的计算函数（y轴负半轴位置）
def tilt_flame_rad_heat_pc(H, R, theta, epsilon, T, rad_heat):
    try:
        Y_c = Symbol('Y_c')
        #rad_heat=rad_heat
        #R_c=0
        #Example:
        #H=20
        #X=50
        theta=theta/180*pi
        a=H/R
        b=Y_c/R
        FV2=-(a**2*sin(theta)*cos(theta)/(4*pi*(b**2+a**2*sin(theta)*sin(theta))))*log((a**2+b**2-1-2*a*pow((b**2-1),0.5)*sin(theta)/b)/(a**2+b**2-1+2*a*pow((b**2-1),0.5)*sin(theta)/b))+cos(theta)/(2*pi*pow((b**2-sin(theta)*sin(theta)),0.5))\
            *(atan((a*b/pow(b**2-1,0.5)+sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5)))+atan((a*b/pow(b**2-1,0.5)-sin(theta))/(pow(b**2-sin(theta)*sin(theta),0.5))))-a*b*cos(theta)/(pi*(b**2+a**2*sin(theta)*sin(theta)))\
            *atan(pow(((b-1)/(b+1)),0.5))+(a*b*cos(theta)*(a**2+b**2+1))/(2*pi*(b**2+a**2*sin(theta)*sin(theta))*pow((pow(a**2+b**2+1,2)-4*(b**2+a**2*sin(theta)*sin(theta))),0.5))\
            *(atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)-2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5)))+atan(((a**2+(b+1)**2)*pow((b-1)/(b+1),0.5)+2*a*sin(theta))/(pow(((pow((a**2+b**2+1),2))-(4*(b**2+a**2*sin(theta)*sin(theta)))),0.5))))
        #This is for test:f_qv_r0=FV1-0.118
        #for i in range(5):
        func_qh_yc=FV2*E-rad_heat
        result=nsolve(func_qh_yc, Y_c, R+0.3) # 20 is the initial guess, this is required for nsolve function
        Y_c=result
        #this is the Hazardous Radius (5 values)
        print(Y_c)
        return(Y_c)
    except Exception as e:
        return 0
        traceback.print_exc()


#plot abc circle
def plot_abc(H, R, theta, rad, fig):
    try:
        X_a=tilt_flame_rad_heat_pa(H, R, theta, rad)
        X_b=tilt_flame_rad_heat_pb(H, R, theta, rad)
        Y_c=tilt_flame_rad_heat_pc(H, R, theta, rad)
        plt.ion()
        plt.clf()


        # fig = plt.figure()
        ax = fig.add_subplot(111)
        R_3=[X_a, X_b, Y_c]
        colors = ["blue","yellow","green"]
        for i in range(3):
            cir = Circle(xy = (0.0, 0.0), radius=R_3[i], alpha=0.5, linewidth=2, fill=False, color= colors[i])
            ax.add_patch(cir)
            x, y = 0, 0
            ax.plot(x, y, 'ro')

            plt.title('Radiation heat flux (3 points)')
            plt.axis('scaled')
            plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

        ax.plot(X_a, 0, 'ro')
        ax.plot((-1)*X_b, 0, 'ro')
        ax.plot(0, (-1)*Y_c, 'ro')

        plt.text(0, 0, 'flame', ha='right', wrap=True)
        plt.text(int(X_a), 0, 'a', ha='right', wrap=True)
        plt.text(int(X_b)*(-1), 0, 'b', ha='left', wrap=True)
        plt.text(0, int(Y_c)*(-1), 'c', ha='left', wrap=True)
        # plt.legend()

        plt.pause(3)
        plt.show()
    except Exception as e:
        traceback.print_exc()
        plt.pause(3)



#传入参数为高度H,火焰半径R,倾角theta
#假设人在沿火焰倾斜方向的热流密度与X的关系
#名称：沿火焰倾斜方向的热流密度沿X轴分布
#draw_rad_heat_flux_curve_FH1_x_pos(50, 15, 45)
#draw_rad_heat_flux_curve_FH1_x_neg(50, 15, 45)
#draw_rad_heat_flux_curve_FH2_y_vertical(50, 15, 45)

#draw_rad_heat_flux_curve_FV1_x_pos(50, 15, 45)
#draw_rad_heat_flux_curve_FV1_x_neg(50, 15, 45)
#draw_rad_heat_flux_curve_FV2_y_vertical(50, 15, 45)

#假设人在垂直火焰倾斜方向的热流密度与X的关系
#名称：垂直火焰倾斜方向的热流密度沿Y轴分布
#draw_rad_heat_flux_curve_FV2(50, 15, 45)

#当热流密度为4kW/m2时，找出对应4 kW/m2时a点、b点、c点的位置，以这些位置为半径，分别化同心圆
#名称：以火焰中心为中心的伤害范围示意图
# plot_abc(18, 13, 75, 4)

#假设人在a点的伤害半径
#名称：假设人在a点不同辐射热流值的伤害范围
# tilt_flame_hazardous_radius_xa(0.17, 0.85, 70)
# #名称：假设人在b点不同辐射热流值的伤害范围
# tilt_flame_hazardous_radius_xb(0.17, 0.85, 70)
# #名称：假设人在c点不同辐射热流值的伤害范围
# tilt_flame_hazardous_radius_xc(0.17, 0.85, 70)



