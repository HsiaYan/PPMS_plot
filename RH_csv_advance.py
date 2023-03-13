
import pandas as pd
import tkinter.messagebox
import getpass


def RH_csv_process(RH_csv_path, len_wid_thick):
    user = getpass.getuser()
    data_frame_num = pd.ExcelFile(RH_csv_path)
    for i in data_frame_num.sheet_names:
        data_frame = (
            pd.read_excel(RH_csv_path, sheet_name=i, names=['Temperature+', 'Mag+', 'Bridge1+', 'Bridge2+', 'Bridge3+',
                                                            'Temperature-', 'Mag-', 'Bridge1-', 'Bridge2-',
                                                            'Bridge3-']))
        P_list = data_frame['Mag+'].dropna(axis=0, how='any').values.tolist()
        M_list = data_frame['Mag-'].dropna(axis=0, how='any').values.tolist()
        data_frame_P = data_frame.iloc[:, 0:5].dropna(axis=0, how='any')  # Define the empty column for final storage
        data_p = {'Temperature+': [], 'Mag+': [], 'Bridge1+': [], 'Bridge2+': [], 'Bridge3+': []}
        P_frame = pd.DataFrame(data_p)
        data_frame_M = data_frame.iloc[:, 5:13].dropna(axis=0, how='any')
        data_m = {'Temperature-': [], 'Mag-': [], 'Bridge1-': [], 'Bridge2-': [], 'Bridge3-': []}
        M_frame = pd.DataFrame(data_m)
        P_data = []
        M_data = []
        if len(P_list) <= len(M_list):
            for p in P_list:
                data = []
                for m in M_list:
                    data.append(abs(p - abs(m)))  # every minus data
                if M_list[data.index(min(data))] not in M_data:
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

        Tot_Frame = pd.concat([P_frame, M_frame], axis=1)
        len_wid_thick_list = len_wid_thick.split(" ")
        k_area = float(len_wid_thick_list[1]) * float(len_wid_thick_list[2]) / float(len_wid_thick_list[0])
        Tot_Frame['Mag'] = (Tot_Frame['Mag+'] - Tot_Frame['Mag-']) / 2000  # 单位kOe
        # index_Rhoxx = Tot_Frame['Mag'].dropna(axis=0, how='any').values.tolist().index(min(Tot_Frame['Mag'].dropna(axis=0, how='any').values.tolist()))
        index_Rhoxx = Tot_Frame['Mag'].dropna(axis=0, how='any').values.tolist().index(min(Tot_Frame['Mag'].dropna(axis=0, how='any').values.tolist()))
        if len_wid_thick_list[-1] == "1":
            Tot_Frame['Rho_xy'] = (Tot_Frame['Bridge1+'] - Tot_Frame['Bridge1-']) / 2 * float(len_wid_thick_list[2]) * 100000  # hall
            Tot_Frame['Rho_xx'] = (Tot_Frame['Bridge2+'] + Tot_Frame['Bridge2-']) / 2 * k_area * 100000  # 直流
            Tot_Frame['Sigma_xy'] = abs(Tot_Frame['Rho_xy'] / Tot_Frame['Rho_xx'] / Tot_Frame ['Rho_xx']) * 1000000  # 电导率
            Tot_Frame['MR'] = (Tot_Frame['Rho_xx'] - Tot_Frame.loc[index_Rhoxx, 'Rho_xx']) * 100  # MR
        elif len_wid_thick_list[-1] == "3":
            Tot_Frame['Rho_xy'] = (Tot_Frame['Bridge3+'] - Tot_Frame['Bridge3-']) / 2 * float(len_wid_thick_list[2]) * 100000
            Tot_Frame['Rho_xx'] = (Tot_Frame['Bridge2+'] + Tot_Frame['Bridge2-']) / 2 * k_area * 100000
            Tot_Frame['Sigma_xy'] = abs(Tot_Frame['Rho_xy'] / Tot_Frame['Rho_xx'] / Tot_Frame['Rho_xx']) * 1000000
            Tot_Frame['MR'] = (Tot_Frame['Rho_xx'] - Tot_Frame[index_Rhoxx + 1, 'Rho_xx']) * 100
        else:
            tkinter.messagebox.showinfo('提示', "长宽高的输入格式有误，请检查输入")

        Tot_Frame.to_csv('C:/Users/' + user + '/Desktop/' + str(i) + '.dat', index=False,
                                                     encoding='utf8')
    tkinter.messagebox.showinfo('提示', "剔除数据完成，输出文件集合在桌面。")