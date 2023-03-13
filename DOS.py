def Dos_process(dos_path, nedos):
    import pandas as pd
    import tkinter.messagebox
    import getpass

    list_dos = []
    data_frame = pd.read_csv(dos_path, header=None, sep='\\s+')
    data_frame.dropna(axis=0, how='all')
    dataframe_row = data_frame.shape[0]
    user = getpass.getuser()
    num = 1
    for i in range(0, dataframe_row, nedos*2):
        dataframe_part = data_frame.iloc[i:nedos * 2 * num, :]
        dataframe_part = dataframe_part.reset_index(drop=True)
        list_dos.append(dataframe_part)
        num += 1
    pd.concat(list_dos, axis=1).to_csv('C:/Users/' + user + '/Desktop/DOS.dat', index=False, header=None)
    tkinter.messagebox.showinfo('提示', "完成！文件在桌面~~~~")
