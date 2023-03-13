import matplotlib.pyplot as plt
import pandas as pd


def Plot_MH_process(MH_path,Mass):
    data_frame = pd.read_csv(MH_path)  # read fil
    num = 1
    while num < data_frame.shape[1]:
        mag = (data_frame.iloc[:, num] / 1000).values.tolist()
        mom = (data_frame.iloc[:, num + 1]/Mass).values.tolist()
        label_str = str(data_frame.iloc[0, num - 1]) + 'K'
        plt.plot(mag, mom, label=label_str)
        num += 3
    plt.title("MH")
    plt.xlabel("H (kOe)")
    plt.ylabel("M (emu/g)")
    plt.legend()
    plt.show()

