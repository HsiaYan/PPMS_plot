import matplotlib.pyplot as plt
import pandas as pd
import os


def getFileName(path):
    f_list = os.listdir(path)  # 返回文件名
    for i in f_list:
        if os.path.splitext(i)[1] == '.dat':
            data_frame = pd.read_csv(path+'/'+i)  # read fil
            mag = data_frame.iloc[:, -5].values.tolist()
            Rxy = data_frame.iloc[:, -4].values.tolist()
            Rxx = data_frame.iloc[:, -3].values.tolist()
            Sigmaxy = data_frame.iloc[:, -2].values.tolist()
            MR = data_frame.iloc[:, -1].values.tolist()
            label_str = os.path.splitext(i)[0]
            plt.figure(1)
            plt.title("Rxy(H)")
            plt.xlabel("H (kOe)")
            plt.ylabel("Rho_xy (uOhm cm)")
            plt.plot(mag, Rxy, label=label_str)
            plt.figure(2)
            plt.title("Rxx(H)")
            plt.xlabel("H (kOe)")
            plt.ylabel("Rho_xx (uOhm cm)")
            plt.plot(mag, Rxx, label=label_str)
            plt.figure(3)
            plt.title("Sigma_xy(H)")
            plt.xlabel("H (kOe)")
            plt.ylabel("Sigma_xy(S/cm)")
            plt.plot(mag, Sigmaxy, label=label_str)
            plt.figure(4)
            plt.title("MR")
            plt.xlabel("H (kOe)")
            plt.ylabel("MR(%)")
            plt.plot(mag, MR, label=label_str)
        else:
            continue
    plt.legend()
    plt.show()
