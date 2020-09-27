import upright_flame_model_v3 as ufm
import tilt_flame_model_v2 as tfm
import  multiprocessing as mp
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

    def run(self):
        self.readProcess.start()

    def dealHandle(self,queue):
        print("Process is reading ....")
        while True:
            if(self.flag == False):
                print("False")
            else:
                msg = queue.get(True)
                for key in msg.keys():
                    if(msg[key] == True):
                        # print(key)
                        self.algorithmMap[key] = True
                for item in self.algorithmMap.items():
                        if(item[1] == True):
                            eval(item[0])



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