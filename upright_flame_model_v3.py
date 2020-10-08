#最后七行是显示的调用函数
#line249-1999是两个样本数据，仅供测试，可以删除

#5、垂直圆柱火焰模型视角系数
from sympy import Symbol, sqrt, cos, sin, atan, log, nsolve, solveset,solve
from matplotlib.patches import Circle, Rectangle
import matplotlib.pyplot as plt
import numpy as np
import math,traceback
# import scipy.interpolate as spi

#L表示圆柱体火焰的高度
#d表示圆柱体火焰直径
#r表示圆柱中心线到目标微元的水平距离
#l=2*L/d
pi= np.pi
#epsilon=0.5
sigma=5.6697*(10**(-8))

#暂时不用
def tempCal(H):
    if (0<H and H<206.43):   #(0<H/100/13.7055<0.1)(137.055 155.481 177.253 192.076 206.43)
        T=973.8*(H/2064.3)**0.028+273.15
    elif (206.43<H and H<309.6450):  #(0.1<H/100/13.7055<0.15)(205.5828 233.2215  265.8795  288.1140  309.6450)
        T=52.99*(H/2064.3)**(-1.22)+273.15
    elif (H>309.6450):  #(H/100/13.7055>0.15)
        T=16.91*(H/2064.3)**(-1.788)+273.15
    return T

#垂直表面jv接收的来自整个火焰的辐射热流
#For point (r,z), calculate the q value
def d_flame_fitting(d_original, height_original, layer_thickness):
    Height=np.max(height_original)
    layerNum=math.ceil(Height/layer_thickness)
    H_array=np.linspace(0,Height,layerNum)

    x=height_original
    y=d_original
    exponential_number=8
    f1 = np.polyfit(x[1:len(x)-1], y[1:len(y)-1], exponential_number)
    d_flame=np.polyval(f1, H_array)
    # in curve fitting, we need to avoid d_flame <= 0
    d_flame[d_flame <= 0] = 0.001
    return d_flame

def heat_flux_v(d_flame, height_original, z_height, layer_thickness, x_distance):
    #z：观测点高度
    #d_flame:火焰直径，array
    #Height:火焰高度
    #L:火焰高度
    #x_distance:圆柱边缘到目标微元的水平距离
    Height=np.max(height_original)
    layerNum=math.ceil(Height/layer_thickness)
    H_array=np.linspace(Height/layerNum,Height,layerNum)
    Qv_total=0.0    
    k=-3.674
    z=z_height
    i=0
    r=max(d_flame)/2+x_distance
    #r表示圆柱中心线到目标微元的水平距离
    for i in range (0,layerNum):
        H=H_array[i]
        if (d_flame[i]==0):
            d_flame[i]=0.01
        S=2*r/d_flame[i]
        h1=2*(H+layer_thickness-z)/d_flame[i]
        h2=2*(H-z)/d_flame[i]
        A1=(h1**2+S**2+1)/(2*S)
        A2=(h2**2+S**2+1)/(2*S)
        #EQ(13)
        Fv1=(1/(pi*S))*atan(h1/sqrt(S**2-1))-(h1/(pi*S))*atan(sqrt((S-1)/(S+1)))+(A1*h1)/(pi*S*sqrt(A1**2-1))*atan(sqrt(((A1+1)*(S-1))/((A1-1)*(S+1))))
       
        Fv2=(1/(pi*S))*atan(h2/sqrt(S**2-1))-(h2/(pi*S))*atan(sqrt((S-1)/(S+1)))+(A2*h2)/(pi*S*sqrt(A2**2-1))*atan(sqrt(((A2+1)*(S-1))/((A2-1)*(S+1))))
        Fv=Fv1-Fv2
        #print(Fv1)
        T=600 #tempreture
        #T=tempCal(H)
        epsilon=1-math.e**(k*d_flame[i]) #发射率
        E=sigma*epsilon*(T**4)

        qv=Fv*E 
        Qv_total=Qv_total+qv #EQ(6)
    return Qv_total
    #print(Qv_total)

def draw_rad_heat_flux_curve_Fv(d_flame, height_original, layer_thickness, x_distance):
    #d_flame:火焰直径，array
    #x_distance是水平方向上观测点与火焰的距离
    try:
        plt.ion()
        z_height=np.max(height_original)
        h = np.arange(z_height/100, z_height, z_height/100) #Radius
        y = []
        for h_dis in h:
            try:
                y_1 = heat_flux_v(d_flame, height_original, h_dis, layer_thickness, x_distance)
                y.append(y_1)
            except Exception as e:
                print(e)
        plt.clf()
        plt.plot(h, y, label="Radiative heat flux")
        plt.title('Radiative heat flux curve for upright flame--vertical direction')
        plt.xlabel("Height of observation (m)")
        plt.ylabel("Radiative heat flux (kW/m^2)")
        plt.text(0.01, 0.01, 'r='+str(int(x_distance))+" m", wrap=True)
        plt.legend()
        plt.pause(3)
        plt.show()
    except Exception as e:
        traceback.print_exc()
        plt.pause(2)
#相同半径的圆上热流密度分布

def draw_rad_heat_flux_vertical_view(d_original, height_original, layer_thickness,x_distance, fig):
    try:
        plt.ion()
        z_height=np.max(height_original)
        x = np.arange(z_height/5, z_height, z_height/5) #Radius
        y = []
        # fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111)
        #bx = fig.add_subplot(122)

        for x_dis in x:
            try:
                y_1 = heat_flux_v(d_original, height_original, x_dis, layer_thickness, x_distance)
                print(y_1)
                y.append(y_1)
                cir = Circle(xy = (0.0, 0.0), radius=x_dis, alpha=0.5, facecolor= (0.1,0.7,0.5,x_dis*0.01))
                ax.add_patch(cir)
                plt.axis('scaled')
                plt.axis('equal')
            except Exception as e:
                print(e)
        ax.plot(0, 0, 'ro') #flame
        plt.text(layer_thickness, 0, str(round(y[0],3))+" kW/m^2", wrap=True)
        plt.text(x_dis, 0, str(round(y[-1], 3))+" kW/m^2", wrap=True)
        plt.title('Heat Flux distribution (Vertical View)')
        plt.xlabel("Distance to flame (m)")
        plt.ylabel("Distance to flame (m)")
        plt.pause(3)
        plt.show()

    except Exception as e:
        traceback.print_exc()
        plt.pause(3)

#水平表面jH接收的来自整个火焰的辐射热流
#每个r处的heat_flux_h
def heat_flux_h(d_flame, height_original, layer_thickness, R_distance):
    #z=0
    #d_flame:火焰直径，array
    #Height:火焰高度
    #L:火焰高度
    Height=np.max(height_original)
    layerNum=math.ceil(Height/layer_thickness)
    H_array=np.linspace(layer_thickness,Height,layerNum)

    Qh_total=0    
    k=-3.674
    r=R_distance
    i=0
    #r表示圆柱中心线到目标微元的水平距离
    for i in range (1,layerNum):
        H=H_array[i]
        S=2*r/d_flame[i]
        B=(1+S**2)/(2*S)

        h1=2*(H+layer_thickness)/d_flame[i]
        h2=2*H/d_flame[i]
        A1=(h1**2+S**2+1)/(2*S)
        A2=(h2**2+S**2+1)/(2*S)

        Fh1=(B-1/S)/(pi*sqrt(B**2-1))*atan(sqrt((B+1)*(S-1)/(B-1)/(S+1)))-(A1-1/S)/(pi*sqrt(A1**2-1))*atan(sqrt((A1+1)*(S-1)/(A1-1)/(S+1)))
        Fh2=(B-1/S)/(pi*sqrt(B**2-1))*atan(sqrt((B+1)*(S-1)/(B-1)/(S+1)))-(A2-1/S)/(pi*sqrt(A2**2-1))*atan(sqrt((A2+1)*(S-1)/(A2-1)/(S+1)))

        Fh=Fh1-Fh2
        #print(Fh)
        T=600 #tempreture
        #T=tempCal(H)
        epsilon=1-math.e**(k*d_flame[i]) #发射率
        E=sigma*epsilon*(T**4)
        qh=Fh*E
        Qh_total=Qh_total+qh
    return Qh_total
    #print(Qh_total)

def draw_rad_heat_flux_curve_Fh(d_flame, height_original, R_distance_max, layer_thickness):
    rad_heat=[1.6,4.0,12.5,25.0,37.5]
    fig = plt.figure()
    try:
        plt.ion()
        #d_flame:火焰直径，array
        x = np.arange(max(d_flame), R_distance_max, (R_distance_max-(max(d_flame)))/10) #Radius
        y = []
        for x_dis in x:
            y_1 = heat_flux_h(d_flame, height_original, layer_thickness, x_dis)
            y.append(y_1)
        plt.clf()
        plt.title('Radiative heat flux curve for upright flame--horizontal direction')
        plt.plot(x, y, label="Radiative heat flux")
        plt.xlabel("Distance to flame (m)")
        plt.ylabel("Radiative heat flux (kW/m^2)")
        plt.legend()
        plt.pause(3)
        plt.show()

        #拟合曲线，计算5个Radiation对应的X_a
        x_xa=np.array(y)
        x_xa=x_xa.astype(np.float64)
        y_xa=x
        exponential_number=8
        f2 = np.polyfit(x_xa, y_xa, exponential_number)
        X_a_array=np.polyval(f2, rad_heat)
        print(X_a_array)
        X_a_array[X_a_array<0]=0

    except Exception as e:
        traceback.print_exc()

    # return X_a_array

def flame_hazardous_radius_xa(X_a_array, fig):
    ax = fig.add_subplot(111)
    colors = ["orange","cyan","pink","lime","yellow"]
    for i in range(5):
        try:
            cir = Circle(xy = (0.0, 0.0), radius=X_a_array[i], facecolor= colors[i]) #alpha=0.5,
            ax.add_patch(cir)
            x, y = 0, 0
            ax.plot(x, y, 'ro')
            #ax.arrow(0,0,int(R_5[i]),i*10,length_includes_head = True, head_width = 2, head_length = 2,fc = 'k',ec = 'k')
            plt.text(int(X_a_array[i]), i*10, str(int(X_a_array[i])), ha='right', wrap=True, rotation='vertical')
            plt.title('Hazardous Radius for the upright flame(5 levels)')
            plt.axis('scaled')
            plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
        except :
            continue
    plt.pause(5)
    plt.show()


def flame_hazardous_radius_xa(d_flame, height_original, R_distance_max, layer_thickness, rad_heat, fig):
    ax = fig.add_subplot(132)

    x, y = calculate_rad_heat_flux_curve_Fh(d_flame, height_original, R_distance_max, layer_thickness)
    # 拟合曲线，计算5个Radiation对应的X_a
    x_xa = np.array(y)
    x_xa = x_xa.astype(np.float64)
    y_xa = x
    exponential_number = 8
    f2 = np.polyfit(x_xa, y_xa, exponential_number)
    X_a_array = np.polyval(f2, rad_heat)
    # print(X_a_array)
    X_a_array[X_a_array < 0] = 0

    colors = ["orange", "cyan", "pink", "lime", "yellow"]
    for i in range(5):
        try:
            cir = Circle(xy=(0.0, 0.0), radius=X_a_array[i], facecolor=colors[i])  # alpha=0.5,
            ax.add_patch(cir)
            x, y = 0, 0
            ax.plot(x, y, 'ro')
            # ax.arrow(0,0,int(R_5[i]),i*10,length_includes_head = True, head_width = 2, head_length = 2,fc = 'k',ec = 'k')
            plt.text(int(X_a_array[i]), i * 10, str(int(X_a_array[i])), ha='right', wrap=True, rotation='vertical')
            plt.title('Hazardous Radius for the upright flame(5 levels)')
            plt.axis('scaled')
            plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length
        except:
            continue
    plt.pause(0.04)
    plt.show()


#height_original是在一帧图像上提取的每一层火焰高度，数组
#d_original是在一帧图像上提取的每一层火焰直径，数组
#these are two examples of extracted height_original and d_original

layer_thickness=0.01
#d_flame= d_flame_fitting(d_original, height_original, layer_thickness)
d_flame=[0.01, 0.7, 0.66, 0.61, 0.58, 0.55, 0.53, 0.54, 0.5, 0.48, 0.45, 0.45, 0.41, 0.36, 0.32, 0.28, 0.28, 0.26, 0.22, 0.19, 0.13, 0.08, 0.06, 0.03, 0.06, 0.07, 0.11]
height_original=np.array([0.16, 0.15, 0.14, 0.13, 0.13, 0.12, 0.11, 0.11, 0.1, 0.09, 0.09, 0.08, 0.07, 0.07, 0.06, 0.05, 0.05, 0.04, 0.03, 0.03, 0.02, 0.01, 0.01])

# four key display functions 

R_distance_max=5#这个参数是绘制曲线时x轴的范围，应大于火焰半径

#垂直圆柱体火焰在水平方向热流密度分布
#垂直圆柱体火焰伤害半径示意图
# draw_rad_heat_flux_curve_Fh(d_flame, height_original, R_distance_max, layer_thickness)

#垂直圆柱体火焰垂直方向的热流密度分布
#x_distance=1#这个参数是圆柱外边缘到目标微元的水平距离，是一个给定的参数
#draw_rad_heat_flux_curve_Fv(d_flame, height_original, layer_thickness, x_distance)

#垂直圆柱体火焰热流密度分布俯视图
#draw_rad_heat_flux_vertical_view(d_flame, height_original, layer_thickness)

#绘制5个不同热流对应的距离火焰的半径（5个同心圆）
# flame_hazardous_radius_xa(X_a_array, fig)
#Notes: layer_thickness need to be set based on the specific circumstance. Here it is 0.01


