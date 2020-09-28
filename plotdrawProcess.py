import upright_flame_model_v3 as ufm
import tilt_flame_model_v2 as tfm
import  multiprocessing as mp
import time
import matplotlib.pyplot as plt

class PlotProcess:
    def __init__(self,queue_):
        self.queue = queue_
        self.readProcess = mp.Process(target=self.dealHandle,args=(self.queue,))
        self.flag = True
        self.algorithmMap = {"draw_rad_heat_flux_curve_FH1":False,
                            "draw_rad_heat_flux_curve_FV2" :False,
                            "plot_abc" : False,
                            "tilt_flame_hazardous_radius_xa":False,
                            "tilt_flame_hazardous_radius_xb":False,
                             "tilt_flame_hazardous_radius_xc":False,
                             "draw_rad_heat_flux_curve_Fh":False,
                             "draw_rad_heat_flux_curve_Fv":False,
                             "draw_rad_heat_flux_vertical_view":False,
                             "flame_hazardous_radius_xa":False
                             }

    def handle_close_draw_rad_heat_flux_curve_FH1(self):
        print("close")
        self.algorithmMap['draw_rad_heat_flux_curve_FH1'] = False

    def handle_close_plot_abc(self):
        pass

    def handle_close_tilt_flame_hazardous_radius_xa(self):
        pass
    def handle_close_tilt_flame_hazardous_radius_xb(self):
        pass
    def handle_close_tilt_flame_hazardous_radius_xc(self):
        pass
    def handle_close_draw_rad_heat_flux_curve_Fh(self):
        pass
    def handle_close_draw_rad_heat_flux_curve_Fv(self):
        pass
    def handle_close_draw_rad_heat_flux_vertical_view(self):
        pass
    def handle_close_flame_hazardous_radius_xa(self):
        pass


    def figureInit(self):
        self.fig_draw_rad_heat_flux_curve_FH1 =  plt.figure("draw_rad_heat_flux_curve_FH1")
        self.fig_plot_abc = plt.figure("plot_abc")
        self.fig_tilt_flame_hazardous_radius_xa = plt.figure("tilt_flame_hazardous_radius_xa")
        self.fig_tilt_flame_hazardous_radius_xb = plt.figure("tilt_flame_hazardous_radius_xb")
        self.fig_tilt_flame_hazardous_radius_xc = plt.figure("tilt_flame_hazardous_radius_xc")
        self.fig_draw_rad_heat_flux_curve_Fh = plt.figure("draw_rad_heat_flux_curve_Fh")
        self.fig_draw_rad_heat_flux_curve_Fv = plt.figure("draw_rad_heat_flux_curve_Fv")
        self.fig_draw_rad_heat_flux_vertical_view = plt.figure("draw_rad_heat_flux_vertical_view")
        self.fig_flame_hazardous_radius_xa = plt.figure("flame_hazardous_radius_xa")



        self.fig_draw_rad_heat_flux_curve_FH1.canvas.mpl_connect('close_event', self.handle_close_draw_rad_heat_flux_curve_FH1)
        self.fig_plot_abc.canvas.mpl_connect("close_event", self.handle_close_plot_abc )
        self.fig_tilt_flame_hazardous_radius_xa.canvas.mpl_connect("close_event", self.handle_close_flame_hazardous_radius_xa)
        self.fig_tilt_flame_hazardous_radius_xb.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xb)
        self.fig_tilt_flame_hazardous_radius_xc.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xc)
        self.fig_draw_rad_heat_flux_curve_Fh.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_curve_Fh)
        self.fig_draw_rad_heat_flux_curve_Fv.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_curve_Fv)
        self.fig_draw_rad_heat_flux_vertical_view.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_vertical_view)
        self.fig_flame_hazardous_radius_xa.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xa)





    def run(self):
        self.readProcess.start()

    def dealHandle(self,queue):
        print("Process is reading ....")
        while True:
                msg = queue.get(True)
                for key in msg.keys():
                    if(msg[key] == True):
                        print(key)
                        self.algorithmMap[key] = True
                fireHeight = msg['fireHeight']
                fireWidget = msg['fireWidget']
                angle = msg['angle']
                fireLayerDiameter = msg['fireLayerDiameter']
                fireLayerHeight = msg['fireLayerHeight']

                if(self.algorithmMap['draw_rad_heat_flux_curve_FH1'] == True):
                    print("draw_rad_heat_flux_curve_FH1")
                    tfm.draw_rad_heat_flux_curve_FH1(fireHeight, fireWidget, angle)
                    # time.sleep(1)
                if(self.algorithmMap['draw_rad_heat_flux_curve_FV2'] == True):
                    tfm.draw_rad_heat_flux_curve_FV2(fireHeight, fireWidget, angle)

                if(self.algorithmMap['plot_abc'] == True):
                    pass
                if(self.algorithmMap['tilt_flame_hazardous_radius_xa'] == True):
                    pass
                if(self.algorithmMap['tilt_flame_hazardous_radius_xb'] == True):
                    pass
                if(self.algorithmMap['tilt_flame_hazardous_radius_xc'] == True):
                    pass
                if(self.algorithmMap['draw_rad_heat_flux_curve_Fh'] == True):
                    pass
                if(self.algorithmMap['draw_rad_heat_flux_curve_Fv'] == True):
                    pass
                if(self.algorithmMap['draw_rad_heat_flux_vertical_view'] == True):
                    pass
                if(self.algorithmMap['flame_hazardous_radius_xa'] == True):
                    pass



    def set(self):
        print("set")
        self.flag = False




if __name__ == '__main__':

    queue = mp.Queue()
    pltP = PlotProcess(queue)
    pltP.run();
    queue.put(1)
    queue.put(2)
    pltP.set()
    queue.put(3)