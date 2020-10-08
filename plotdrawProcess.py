import upright_flame_model_v6 as ufm
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
        # self.figureInit()
        self.created_draw_rad_heat_flux_curve_FH1 = False
        self.created_draw_rad_heat_flux_curve_FV2 = False

    def handle_close_draw_rad_heat_flux_curve_FH1(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FH1'] = False

        self.created_draw_rad_heat_flux_curve_FH1= False

    def handle_close_draw_rad_heat_flux_curve_FV2(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FV2'] = False
        self.created_draw_rad_heat_flux_curve_FV2= False

    def handle_close_plot_abc(self, evt):
        self.algorithmMap['plot_abc'] = False

    def handle_close_tilt_flame_hazardous_radius_xa(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xa'] = False

    def handle_close_tilt_flame_hazardous_radius_xb(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xb'] = False

    def handle_close_tilt_flame_hazardous_radius_xc(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xc'] = False

    def handle_close_draw_rad_heat_flux_curve_Fh(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_Fh'] = False

    def handle_close_draw_rad_heat_flux_curve_Fv(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_Fv'] = False

    def handle_close_draw_rad_heat_flux_vertical_view(self, evt):
        self.algorithmMap['draw_rad_heat_flux_vertical_view'] =False

    def handle_close_flame_hazardous_radius_xa(self, evt):
        self.algorithmMap['flame_hazardous_radius_xa'] = False



    # def figureInit(self):
    #     self.fig_draw_rad_heat_flux_curve_FH1 =  plt.figure("draw_rad_heat_flux_curve_FH1")
    #     self.fig_plot_abc = plt.figure("plot_abc")
    #     self.fig_tilt_flame_hazardous_radius_xa = plt.figure("tilt_flame_hazardous_radius_xa")
    #     self.fig_tilt_flame_hazardous_radius_xb = plt.figure("tilt_flame_hazardous_radius_xb")
    #     self.fig_tilt_flame_hazardous_radius_xc = plt.figure("tilt_flame_hazardous_radius_xc")
    #     self.fig_draw_rad_heat_flux_curve_Fh = plt.figure("draw_rad_heat_flux_curve_Fh")
    #     self.fig_draw_rad_heat_flux_curve_Fv = plt.figure("draw_rad_heat_flux_curve_Fv")
    #     self.fig_draw_rad_heat_flux_vertical_view = plt.figure("draw_rad_heat_flux_vertical_view")
    #     self.fig_flame_hazardous_radius_xa = plt.figure("flame_hazardous_radius_xa")
    #
    #
    #
    #     self.fig_draw_rad_heat_flux_curve_FH1.canvas.mpl_connect('close_event', self.handle_close_draw_rad_heat_flux_curve_FH1)
    #     self.fig_plot_abc.canvas.mpl_connect("close_event", self.handle_close_plot_abc )
    #     self.fig_tilt_flame_hazardous_radius_xa.canvas.mpl_connect("close_event", self.handle_close_flame_hazardous_radius_xa)
    #     self.fig_tilt_flame_hazardous_radius_xb.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xb)
    #     self.fig_tilt_flame_hazardous_radius_xc.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xc)
    #     self.fig_draw_rad_heat_flux_curve_Fh.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_curve_Fh)
    #     self.fig_draw_rad_heat_flux_curve_Fv.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_curve_Fv)
    #     self.fig_draw_rad_heat_flux_vertical_view.canvas.mpl_connect("close_event", self.handle_close_draw_rad_heat_flux_vertical_view)
    #     self.fig_flame_hazardous_radius_xa.canvas.mpl_connect("close_event", self.handle_close_tilt_flame_hazardous_radius_xa)
    #




    def run(self):
        self.readProcess.start()

    def dealHandle(self,queue):
        print("Process is reading ....")
        while True:
                msg = queue.get(True)
                print(1)
                for key in msg.keys():
                    if(msg[key] == True):
                        self.algorithmMap[key] = True
                fireHeight = msg['fireHeight']
                fireWidget = msg['fireWidget']
                angle = msg['angle']
                fireLayerDiameter = msg['fireLayerDiameter']
                fireLayerHeight = msg['fireLayerHeight']
                # R_distance = msg['R_distance']
                # time.sleep(1)

                # x, y =  ufm.calculate_rad_heat_flux_curve_Fh(fireLayerDiameter, fireLayerHeight,R_distance)
                if(self.algorithmMap['draw_rad_heat_flux_curve_FH1'] == True):
                    # if(self.created_draw_rad_heat_flux_curve_FH1 == False):
                        self.fig_draw_rad_heat_flux_curve_FH1 = plt.figure("draw_rad_heat_flux_curve_FH1")
                        self.fig_draw_rad_heat_flux_curve_FH1.canvas.mpl_connect('close_event',
                                                                                 self.handle_close_draw_rad_heat_flux_curve_FH1)
                        # self.created_draw_rad_heat_flux_curve_FH1 = True

                        tfm.draw_rad_heat_flux_curve_FH1(fireHeight, fireWidget, angle, self.fig_draw_rad_heat_flux_curve_FH1)
                    # time.sleep(1)
                if(self.algorithmMap['draw_rad_heat_flux_curve_FV2'] == True):
                    if(self.created_draw_rad_heat_flux_curve_FV2 == False):
                        self.fig_draw_rad_heat_flux_curve_FV2 = plt.figure("draw_rad_heat_flux_curve_FV2")
                        self.fig_draw_rad_heat_flux_curve_FV2.canvas.mpl_connect("close_event",
                                                                                 self.handle_close_draw_rad_heat_flux_curve_FV2)
                        # self.created_draw_rad_heat_flux_curve_FV2 = True
                    tfm.draw_rad_heat_flux_curve_FV2(fireHeight, fireWidget, angle, self.fig_draw_rad_heat_flux_curve_FV2)

                if(self.algorithmMap['plot_abc'] == True):
                    self.fig_plot_abc = plt.figure("plot_abc")
                    self.fig_plot_abc.canvas.mpl_connect("close_event",
                                                         self.handle_close_plot_abc)
                    tfm.plot_abc(fireHeight, fireWidget, angle, 4, self.fig_plot_abc)

                if(self.algorithmMap['tilt_flame_hazardous_radius_xa'] == True):
                    self.fig_tilt_flame_hazardous_radius_xa = plt.figure("tilt_flame_hazardous_radius_xa")
                    self.fig_tilt_flame_hazardous_radius_xa.canvas.mpl_connect("close_event",
                                                                               self.handle_close_tilt_flame_hazardous_radius_xa)
                    tfm.tilt_flame_hazardous_radius_xa(fireHeight, fireWidget, angle, self.fig_tilt_flame_hazardous_radius_xa)


                if(self.algorithmMap['tilt_flame_hazardous_radius_xb'] == True):
                    self.fig_tilt_flame_hazardous_radius_xb = plt.figure("tilt_flame_hazardous_radius_xb")
                    self.fig_tilt_flame_hazardous_radius_xb.canvas.mpl_connect("close_event",
                                                                               self.handle_close_tilt_flame_hazardous_radius_xb)
                    tfm.tilt_flame_hazardous_radius_xb(fireHeight, fireWidget, angle, self.fig_tilt_flame_hazardous_radius_xb)


                if(self.algorithmMap['tilt_flame_hazardous_radius_xc'] == True):
                    self.fig_tilt_flame_hazardous_radius_xc = plt.figure("tilt_flame_hazardous_radius_xc")
                    self.fig_tilt_flame_hazardous_radius_xc.canvas.mpl_connect("close_event",
                                                                               self.handle_close_tilt_flame_hazardous_radius_xc)
                    tfm.tilt_flame_hazardous_radius_xc((fireHeight, fireWidget, angle, self.fig_tilt_flame_hazardous_radius_xc))


                if(self.algorithmMap['draw_rad_heat_flux_curve_Fh'] == True):
                    self.fig_draw_rad_heat_flux_curve_Fh = plt.figure("draw_rad_heat_flux_curve_Fh")
                    self.fig_draw_rad_heat_flux_curve_Fh.canvas.mpl_connect("close_event",
                                                                            self.handle_close_draw_rad_heat_flux_curve_Fh)
                    ufm.draw_rad_heat_flux_curve_Fh(fireHeight,fireWidget, angle, self.fig_draw_rad_heat_flux_curve_Fh)

                if(self.algorithmMap['draw_rad_heat_flux_curve_Fv'] == True):
                    self.fig_draw_rad_heat_flux_curve_Fv = plt.figure("draw_rad_heat_flux_curve_Fv")
                    self.fig_draw_rad_heat_flux_curve_Fv.canvas.mpl_connect("close_event",
                                                                            self.handle_close_draw_rad_heat_flux_curve_Fv)
                    ufm.draw_rad_heat_flux_curve_Fv(fireHeight, fireWidget, angle, self.fig_draw_rad_heat_flux_curve_Fv)


                if(self.algorithmMap['draw_rad_heat_flux_vertical_view'] == True):
                    self.fig_draw_rad_heat_flux_vertical_view = plt.figure("draw_rad_heat_flux_vertical_view")
                    self.fig_draw_rad_heat_flux_vertical_view.canvas.mpl_connect("close_event",
                                                                                 self.handle_close_draw_rad_heat_flux_vertical_view)
                    ufm.draw_rad_heat_flux_vertical_view(fireHeight, fireWidget, angle, self.fig_draw_rad_heat_flux_vertical_view)

                if(self.algorithmMap['flame_hazardous_radius_xa'] == True):
                    self.fig_flame_hazardous_radius_xa = plt.figure("flame_hazardous_radius_xa")
                    self.fig_flame_hazardous_radius_xa.canvas.mpl_connect("close_event",
                                                                          self.handle_close_flame_hazardous_radius_xa)
                    # ufm.flame_hazardous_radius_xa()


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