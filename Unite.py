import pandas as pd
import tkinter.messagebox
import getpass

def Unite_process(path1, path2, Bridge1, Bridge2):
    user = getpass.getuser()
    data_frame_num1 = pd.ExcelFile(path1)
    data_frame_num2 = pd.ExcelFile(path2)
    for i in data_frame_num1.sheet_names:
        data_frame1 = (pd.read_excel(RH_csv_path, sheet_name=i, names=['Temperature+', 'Mag+', 'Bridge1+', 'Bridge2+', 'Bridge3+',
                                                              'Temperature-', 'Mag-', 'Bridge1-', 'Bridge2-', 'Bridge3-']))
        if Bridge1 == "1":
            data_frame1 = data_frame1.iloc[:, [0, 1, 2, 5, 6, 7]]
        elif Bridge1 == "3":
            data_frame1 = data_frame1.iloc[:, [0, 1, 4, 5, 6, 9]]
        else:
            pass
    for i in data_frame_num2.sheet_names:
        data_frame2 = (pd.read_excel(RH_csv_path, sheet_name=i, names=['Temperature+', 'Mag+', 'Bridge1+', 'Bridge2+', 'Bridge3+',
                                                              'Temperature-', 'Mag-', 'Bridge1-', 'Bridge2-', 'Bridge3-']))
