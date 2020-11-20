import upright_flame_model_v6 as ufm
import tilt_flame_model_v3 as tfm
import  multiprocessing as mp
import time
import matplotlib.pyplot as plt
import  traceback

class PlotProcess:
    def __init__(self,queue_):
        self.queue = queue_
        self.readProcess = mp.Process(target=self.dealHandle,args=(self.queue,))
        self.flag = True
        self.algorithmMap = {"draw_rad_heat_flux_curve_Fh": False,
                             "draw_rad_heat_flux_curve_Fv": False,
                             "draw_rad_heat_flux_vertical_view": False,
                             "draw_rad_heat_flux_curve_FV1_x_pos": False,
                             "draw_rad_heat_flux_curve_FV1_x_neg": False,
                             "draw_rad_heat_flux_curve_FV2_y_vertical": False,
                             "draw_rad_heat_flux_curve_FH1_x_pos": False,
                             "draw_rad_heat_flux_curve_FH1_x_neg": False,
                             "draw_rad_heat_flux_curve_FH2_y_vertical": False,
                             "flame_hazardous_radius_xa": False,
                             "tilt_flame_hazardous_radius_xa": False,
                             "tilt_flame_hazardous_radius_xb": False,
                             "tilt_flame_hazardous_radius_xc": False,
                             "plot_abc": False
                             }
        # self.figureInit()

        self.created_draw_rad_heat_flux_curve_Fh = False
        self.created_draw_rad_heat_flux_curve_Fv = False
        self.created_draw_rad_heat_flux_vertical_view = False
        self.created_draw_rad_heat_flux_curve_FV1_x_pos = False
        self.created_draw_rad_heat_flux_curve_FV1_x_neg = False
        self.created_draw_rad_heat_flux_curve_FV2_y_vertical = False
        self.created_draw_rad_heat_flux_curve_FH1_x_pos = False
        self.created_draw_rad_heat_flux_curve_FH1_x_neg = False
        self.created_draw_rad_heat_flux_curve_FH2_y_vertical = False
        self.created_flame_hazardous_radius_xa = False
        self.created_tilt_flame_hazardous_radius_xa = False
        self.created_tilt_flame_hazardous_radius_xb = False
        self.created_tilt_flame_hazardous_radius_xc = False
        self.created_plot_abc = False

    def handle_close_draw_rad_heat_flux_curve_Fh(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_Fh'] = False
        self.created_draw_rad_heat_flux_curve_Fh = False

    def handle_close_draw_rad_heat_flux_curve_Fv(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_Fv'] = False
        self.created_draw_rad_heat_flux_curve_Fv = False

    def handle_close_draw_rad_heat_flux_vertical_view(self, evt):
        self.algorithmMap['draw_rad_heat_flux_vertical_view'] = False
        self.created_draw_rad_heat_flux_vertical_view = False

    def handle_close_draw_rad_heat_flux_curve_FV1_x_pos(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FV1_x_pos'] = False
        self.created_draw_rad_heat_flux_curve_FV1_x_pos = False

    def handle_close_draw_rad_heat_flux_curve_FV1_x_neg(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FV1_x_neg'] = False
        self.created_draw_rad_heat_flux_curve_FV1_x_neg = False

    def handle_close_draw_rad_heat_flux_curve_FV2_y_vertical(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FV2_y_vertical'] = False
        self.created_draw_rad_heat_flux_curve_FV2_y_vertical = False

    def handle_close_draw_rad_heat_flux_curve_FH1_x_pos(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FH1_x_pos'] = False
        self.created_draw_rad_heat_flux_curve_FH1_x_pos = False

    def handle_close_draw_rad_heat_flux_curve_FH1_x_neg(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FH1_x_neg'] = False
        self.created_draw_rad_heat_flux_curve_FH1_x_neg = False

    def handle_close_draw_rad_heat_flux_curve_FH2_y_vertical(self, evt):
        self.algorithmMap['draw_rad_heat_flux_curve_FH2_y_vertical'] =False
        self.created_draw_rad_heat_flux_curve_FH2_y_vertical = False

    def handle_close_flame_hazardous_radius_xa(self, evt):
        self.algorithmMap['flame_hazardous_radius_xa'] = False
        self.created_flame_hazardous_radius_xa = False

    def handle_close_tilt_flame_hazardous_radius_xa(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xa'] = False
        self.created_tilt_flame_hazardous_radius_xa = False

    def handle_close_tilt_flame_hazardous_radius_xb(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xb'] = False
        self.created_tilt_flame_hazardous_radius_xb = False

    def handle_close_tilt_flame_hazardous_radius_xc(self, evt):
        self.algorithmMap['tilt_flame_hazardous_radius_xc'] = False
        self.created_tilt_flame_hazardous_radius_xc = False

    def handle_close_plot_abc(self, evt):
        self.algorithmMap['plot_abc'] = False
        self.created_plot_abc = False




    def run(self):
        self.readProcess.start()

    def dealHandle(self,queue):
        print("Process is reading ....")
        while True:
                msg = queue.get(True)
                print(msg)
                for key in msg.keys():
                    if(msg[key] == True):
                        self.algorithmMap[key] = True
                fireHeight = msg['fireHeight']
                fireWidget = msg['fireWidget']
                angle = msg['angle']
                fireLayerDiameter = msg['fireLayerDiameter']
                fireLayerHeight = msg['fireLayerHeight']
                R_distance = msg['R_distance_max']
                rad_heat= msg["RadioThreshold"] #这个也是手动输入的参数
                epsilon = msg['epsilon']
                T = msg['T']
                layer_thickness = msg['layer_thickness']
                fireHeatFluxparam = msg['fireHeatFluxparam']
                observePointHeight = msg['observePointHeight']

                try:
                    x, y =  ufm.calculate_rad_heat_flux_curve_Fh(fireLayerDiameter, fireLayerHeight, R_distance, layer_thickness)
                except Exception as e:
                    traceback.print_exc()

                if (self.algorithmMap['draw_rad_heat_flux_curve_Fh'] == True):
                    try:
                        if (self.created_draw_rad_heat_flux_curve_Fh == False):
                            self.draw_rad_heat_flux_curve_Fh_fig = plt.figure(
                                "draw_rad_heat_flux_curve_Fh")
                            self.draw_rad_heat_flux_curve_Fh_fig.canvas.mpl_connect('close_event',
                                                                                           self.handle_close_draw_rad_heat_flux_curve_Fh)
                            self.created_draw_rad_heat_flux_curve_Fh = True
                        ufm.draw_rad_heat_flux_curve_Fh(x, y, self.draw_rad_heat_flux_curve_Fh_fig)
                    except Exception as e:
                        print(e)

                if (self.algorithmMap['draw_rad_heat_flux_curve_Fv'] == True):
                    try:
                        if (self.created_draw_rad_heat_flux_curve_Fv == False):
                            self.draw_rad_heat_flux_curve_Fv_fig = plt.figure(
                                "draw_rad_heat_flux_curve_Fv")
                            self.draw_rad_heat_flux_curve_Fv_fig.canvas.mpl_connect('close_event',
                                                                                    self.handle_close_draw_rad_heat_flux_curve_Fv)
                            self.created_draw_rad_heat_flux_curve_Fv = True
                        ufm.draw_rad_heat_flux_curve_Fv(fireLayerDiameter, fireLayerHeight, layer_thickness, R_distance, self.draw_rad_heat_flux_curve_Fv_fig)
                    except Exception as e:
                        print(e)


                if (self.algorithmMap['draw_rad_heat_flux_vertical_view'] == True):
                    try:
                        if (self.created_draw_rad_heat_flux_vertical_view == False):
                            self.draw_rad_heat_flux_vertical_view_fig = plt.figure(
                                "draw_rad_heat_flux_vertical_view")
                            self.draw_rad_heat_flux_vertical_view_fig.canvas.mpl_connect('close_event',
                                                                                    self.handle_close_draw_rad_heat_flux_vertical_view)
                            self.created_draw_rad_heat_flux_vertical_view = True
                        ufm.draw_rad_heat_flux_vertical_view(x, y, self.draw_rad_heat_flux_vertical_view_fig)
                    except Exception as e:
                        print(e)


                if(self.algorithmMap['draw_rad_heat_flux_curve_FV1_x_pos'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FV1_x_pos == False):
                            self.draw_rad_heat_flux_curve_FV1_x_pos_fig = plt.figure("draw_rad_heat_flux_curve_FV1_x_pos")
                            self.draw_rad_heat_flux_curve_FV1_x_pos_fig.canvas.mpl_connect('close_event',
                                                                                     self.handle_close_draw_rad_heat_flux_curve_FV1_x_pos)
                            self.created_draw_rad_heat_flux_curve_FV1_x_pos = True
                        tfm.draw_rad_heat_flux_curve_FV1_x_pos(fireHeight, fireWidget, angle, epsilon, T, R_distance, self.draw_rad_heat_flux_curve_FV1_x_pos_fig)
                    except Exception as e:
                        print(e)

                if(self.algorithmMap['draw_rad_heat_flux_curve_FV1_x_neg'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FV1_x_neg == False):
                            self.draw_rad_heat_flux_curve_FV1_x_neg_fig = plt.figure("draw_rad_heat_flux_curve_FV1_x_neg")
                            self.draw_rad_heat_flux_curve_FV1_x_neg_fig.canvas.mpl_connect("close_event",
                                                                                     self.handle_close_draw_rad_heat_flux_curve_FV1_x_neg)
                            self.created_draw_rad_heat_flux_curve_FV1_x_neg = True
                        tfm.draw_rad_heat_flux_curve_FV1_x_neg(fireHeight, fireWidget, angle,  epsilon, T, R_distance, self.draw_rad_heat_flux_curve_FV1_x_neg_fig)
                    except Exception as e:
                        print(e)


                if(self.algorithmMap['draw_rad_heat_flux_curve_FV2_y_vertical'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FV2_y_vertical == False):
                            self.draw_rad_heat_flux_curve_FV2_y_vertical_fig = plt.figure("draw_rad_heat_flux_curve_FV2_y_vertical")
                            self.draw_rad_heat_flux_curve_FV2_y_vertical_fig.canvas.mpl_connect("close_event",
                                                             self.handle_close_draw_rad_heat_flux_curve_FV2_y_vertical)
                            self.created_draw_rad_heat_flux_curve_FV2_y_vertical = True
                        tfm.draw_rad_heat_flux_curve_FV2_y_vertical(fireHeight, fireWidget, angle, epsilon, T, R_distance,  self.draw_rad_heat_flux_curve_FV2_y_vertical_fig)
                    except Exception as e:
                        print(e)

                if(self.algorithmMap['draw_rad_heat_flux_curve_FH1_x_pos'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FH1_x_pos == False):
                            self.fig_draw_rad_heat_flux_curve_FH1_x_pos = plt.figure("draw_rad_heat_flux_curve_FH1_x_pos")
                            self.fig_draw_rad_heat_flux_curve_FH1_x_pos.canvas.mpl_connect("close_event",
                                                                                   self.handle_close_draw_rad_heat_flux_curve_FH1_x_pos)
                            self.created_draw_rad_heat_flux_curve_FH1_x_pos = True
                        tfm.draw_rad_heat_flux_curve_FH1_x_pos(fireHeight, fireWidget, angle,epsilon, T, R_distance, self.fig_draw_rad_heat_flux_curve_FH1_x_pos)
                    except Exception as e:
                        print(e)


                if(self.algorithmMap['draw_rad_heat_flux_curve_FH1_x_neg'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FH1_x_neg == False):

                            self.fig_draw_rad_heat_flux_curve_FH1_x_neg = plt.figure("draw_rad_heat_flux_curve_FH1_x_neg")
                            self.fig_draw_rad_heat_flux_curve_FH1_x_neg.canvas.mpl_connect("close_event",
                                                                               self.handle_close_draw_rad_heat_flux_curve_FH1_x_neg)
                            self.created_draw_rad_heat_flux_curve_FH1_x_neg = True
                        tfm.draw_rad_heat_flux_curve_FH1_x_neg(fireHeight, fireWidget, angle, epsilon, T, R_distance, self.fig_draw_rad_heat_flux_curve_FH1_x_neg)
                    except Exception as e:
                        print(e)

                if(self.algorithmMap['draw_rad_heat_flux_curve_FH2_y_vertical'] == True):
                    try:
                        if(self.created_draw_rad_heat_flux_curve_FH2_y_vertical == False):
                            self.fig_draw_rad_heat_flux_curve_FH2_y_vertical = plt.figure("draw_rad_heat_flux_curve_FH2_y_vertical")
                            self.fig_draw_rad_heat_flux_curve_FH2_y_vertical.canvas.mpl_connect("close_event",
                                                                               self.handle_close_draw_rad_heat_flux_curve_FH2_y_vertical)
                            self.created_draw_rad_heat_flux_curve_FH2_y_vertical = True
                        tfm.draw_rad_heat_flux_curve_FH2_y_vertical(fireHeight, fireWidget, angle,epsilon, R_distance, T, self.fig_draw_rad_heat_flux_curve_FH2_y_vertical)
                    except Exception as e:
                        print(e)

                if(self.algorithmMap['flame_hazardous_radius_xa'] == True):
                    try:
                        if(self.created_flame_hazardous_radius_xa == False):
                            self.fig_flame_hazardous_radius_xa = plt.figure("flame_hazardous_radius_xa")
                            self.fig_flame_hazardous_radius_xa.canvas.mpl_connect("close_event",
                                                                            self.handle_close_flame_hazardous_radius_xa)
                            self.created_flame_hazardous_radius_xa = True
                        ufm.flame_hazardous_radius_xa(x, y, rad_heat, self.fig_flame_hazardous_radius_xa)
                    except Exception as e:
                        print(e)

                if(self.algorithmMap['tilt_flame_hazardous_radius_xa'] == True):
                    try:
                        if(self.created_tilt_flame_hazardous_radius_xa == False):
                            self.fig_tilt_flame_hazardous_radius_xa = plt.figure("tilt_flame_hazardous_radius_xa")
                            self.fig_tilt_flame_hazardous_radius_xa.canvas.mpl_connect("close_event",
                                                                                self.handle_close_tilt_flame_hazardous_radius_xa)
                            self.created_tilt_flame_hazardous_radius_xa = True
                        print(fireHeight)
                        print(fireWidget)
                        tfm.tilt_flame_hazardous_radius_xa(fireHeight, fireWidget, angle, epsilon, T, rad_heat, self.fig_tilt_flame_hazardous_radius_xa)
                    except Exception as e:
                        print(e)



                if(self.algorithmMap['tilt_flame_hazardous_radius_xb'] == True):
                    try:
                        if(self.created_tilt_flame_hazardous_radius_xb == False):
                            self.fig_tilt_flame_hazardous_radius_xb = plt.figure("tilt_flame_hazardous_radius_xb")
                            self.fig_tilt_flame_hazardous_radius_xb.canvas.mpl_connect("close_event",
                                                                                 self.handle_close_tilt_flame_hazardous_radius_xb)
                            self.created_tilt_flame_hazardous_radius_xb = True
                        tfm.tilt_flame_hazardous_radius_xb(fireHeight, fireWidget,  angle, epsilon, T, rad_heat, self.fig_tilt_flame_hazardous_radius_xb)
                    except Exception as e:
                        print(e)


                if(self.algorithmMap['tilt_flame_hazardous_radius_xc'] == True):
                    try:
                        if(self.created_tilt_flame_hazardous_radius_xc == False):
                            self.fig_tilt_flame_hazardous_radius_xc = plt.figure("tilt_flame_hazardous_radius_xc")
                            self.fig_tilt_flame_hazardous_radius_xc.canvas.mpl_connect("close_event",
                                                                          self.handle_close_tilt_flame_hazardous_radius_xc)
                            self.created_tilt_flame_hazardous_radius_xc = True
                        tfm.tilt_flame_hazardous_radius_xc(fireHeight,fireWidget,angle, epsilon, T, rad_heat, self.fig_tilt_flame_hazardous_radius_xc)
                    except Exception as e:
                        print(e)

                ##TODO: 修改
                if (self.algorithmMap['plot_abc'] == True):
                    print("PLOT",fireHeatFluxparam )
                    try:
                        if (self.created_plot_abc == False):
                            self.fig_plot_abc = plt.figure("plot_abc")
                            self.fig_plot_abc.canvas.mpl_connect("close_event",
                                                                            self.handle_close_plot_abc)
                            self.created_plot_abc = True
                        tfm.plot_abc(fireHeight, fireWidget ,angle, epsilon, T, R_distance, fireHeatFluxparam ,self.fig_plot_abc)
                    except Exception as e:
                        print(e)

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