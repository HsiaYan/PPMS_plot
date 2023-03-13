import pandas as pd
import numpy as np
import tkinter.messagebox
import getpass


def MH_process(MH_path):
    user = getpass.getuser()
    list_MH = []

    # data_MH = np.genfromtxt('my_file.csv', delimiter=',')  # read file


    data_frame = pd.read_csv(MH_path)  # read file
    data_frame = data_frame.iloc[:, 2:5]
    data_frame['Temperature (K)'] = round(data_frame['Temperature (K)'])  # The temperature is rounded
    for temperature in data_frame['Temperature (K)'].unique():
        data_list = data_frame.loc[data_frame['Temperature (K)'] == temperature]
        data_list = data_list.reset_index(drop=True)
        list_MH.append(data_list)
    pd.concat(list_MH, axis=1).to_csv('C:/Users/' + user + '/Desktop/MH_output.dat', index=False, header=True)
    tkinter.messagebox.showinfo('提示', "分离完成！输出文件 MH_output.dat 到桌面。")
