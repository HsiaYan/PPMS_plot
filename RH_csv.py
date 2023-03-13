import pandas as pd
import tkinter.messagebox
import getpass


def RH_csv_process(RH_csv_path):
    user = getpass.getuser()
    data_frame_num = pd.ExcelFile(RH_csv_path)
    for i in data_frame_num.sheet_names:
        data_frame = (pd.read_excel(RH_csv_path, sheet_name=i, names=['Temperature+', 'Mag+', 'Bridge1+', 'Bridge2+', 'Bridge3+',
                                                              'Temperature-', 'Mag-', 'Bridge1-', 'Bridge2-', 'Bridge3-']))
        P_list = data_frame['Mag+'].dropna(axis=0, how='any').values.tolist()
        M_list = data_frame['Mag-'].dropna(axis=0, how='any').values.tolist()
        data_frame_P = data_frame.iloc[:, 0:5].dropna(axis=0, how='any')  # Define the empty column for final storage
        data_p = {'Temperature+': [], 'Mag+': [], 'Bridge1+': [], 'Bridge2+': [], 'Bridge3+': []}
        P_frame = pd.DataFrame(data_p)
        data_frame_M = data_frame.iloc[:, 5:10].dropna(axis=0, how='any')
        data_m = {'Temperature-': [], 'Mag-': [], 'Bridge1-': [], 'Bridge2-': [], 'Bridge3-': []}
        M_frame = pd.DataFrame(data_m)
        P_data = []
        M_data = []
        if len(P_list) <= len(M_list):  # 没考虑如果使两列都使齐的情况
            for p in P_list:
                data = []
                for m in M_list:
                    data.append(abs(p - abs(m)))  # 将数据向每一个数据做差，并写入data
                if M_list[data.index(min(data))] not in M_data:  # data最小值的索引对应的M——list的内容，判断是否在data里。
                    M_data.append(M_list[data.index(min(data))]) 
                    P_data.append(p)  # list min >M_data
                else:
                    continue
        else:
            for m in M_list:
                data = []
                for p in P_list:
                    data.append(abs(p - abs(m)))  # every minus data
                if P_list[data.index(min(data))] not in P_data:
                    P_data.append(P_list[data.index(min(data))])
                    M_data.append(m)  # list min >M_data
                else:
                    continue
        for P_i in P_data:
            P_frame = P_frame.append(data_frame_P.loc[data_frame_P['Mag+'] == P_i], ignore_index=True)
        for M_j in M_data:
            M_frame = M_frame.append(data_frame_M.loc[data_frame_M['Mag-'] == M_j], ignore_index=True)
        pd.concat([P_frame, M_frame], axis=1).to_csv('C:/Users/' + user + '/Desktop/'+str(i)+'.dat', index=False, encoding='utf8')
    tkinter.messagebox.showinfo('提示', "剔除数据完成，输出文件集合在桌面。")
