import getpass
import pandas as pd
import tkinter.messagebox


def RH_process(RH_path):
    user = getpass.getuser()
    df = pd.DataFrame()
    df.to_excel('C:/Users/' + user + '/Desktop/RH_data.xlsx')
    writer = pd.ExcelWriter('C:/Users/' + user + '/Desktop/RH_data.xlsx')
    list_minus = []
    list_plus = []

    data_frame = pd.read_csv(RH_path)
    data_frame = data_frame.iloc[:, [3, 4, 6, 8, 10]]
    data_frame.columns = ['Temperature', 'Mag', 'Bridge1', 'Bridge2', 'Bridge3']
    data_frame['Temperature'] = round(data_frame['Temperature'])  # The temperature is rounded

    for temperature in data_frame['Temperature'].unique():
        data_list_minus = data_frame[(data_frame.Temperature == temperature) & (data_frame.Mag < 0)]
        data_list_plus = data_frame[(data_frame.Temperature == temperature) & (data_frame.Mag > 0)]
        data_list_minus = data_list_minus.reset_index(drop=True)  # Reset index
        data_list_plus = data_list_plus.reset_index(drop=True)  # Reset index
        list_minus.append(data_list_minus)
        list_plus.append(data_list_plus)

    for i in range(len(data_frame['Temperature'].unique())):
        pd.concat([list_plus[i], list_minus[i]], axis=1).to_excel(writer, str(data_frame['Temperature'].unique()[i]) + \
                                                                  'K', index=False, header=True)
    writer.save()
    tkinter.messagebox.showinfo('提示', "完成！输出文件 RH_data.xlsx 到桌面。")

# RH_process("C:/Users/HsiaYan/Desktop/Hall-A.dat")
