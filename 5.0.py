from tkinter import Menu  # 导入菜单类
from tkinter.simpledialog import askstring, askfloat
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.messagebox
# 程序函数导入
import Component  # 分子量，配料，磁矩
import MH  # MH数据分离
import RH
import RH_csv
import RH_csv_advance
import Plot_MH
import Plot_RH
import DOS
import EIGENVAL


def _quit():
    """结束主事件循环"""
    win.quit()  # 关闭窗口
    win.destroy()  # 将所有的窗口小部件进行销毁，应该有内存回收的意思
    exit()


def run_Component():
    molecular_str = askstring("", prompt="请输入分子式：")
    Component.Molecular_Weight_Calculator(molecular_str)


def run_mass():
    molecular_mass_str = askstring("", prompt="请输入'质量' 或 '元素 质量'")
    Component.sample_mass(molecular_mass_str)


def run_moment():
    mag_str = askfloat(title="", prompt="请输入磁化强度：emu")
    mass_str = askfloat(title="", prompt="请输入质量：g")
    Component.trans(mag_str, mass_str)


def run_MH():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的dat文件", filetypes=[("dat文件", "*.dat")])
        if file_name_path != '':
            # tkinter.messagebox.showinfo('提示', "稍微等那么一会会儿，好吗？")
            MH.MH_process(file_name_path)
            del file_name_path
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_RH():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的dat文件", filetypes=[("dat文件", "*.dat")])
        if file_name_path != '':
            tkinter.messagebox.showinfo('提示', "稍微等那么一会会儿，好吗？")
            RH.RH_process(file_name_path)
            del file_name_path
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误1")


def run_RH_csv():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的Excel文件", filetypes=[("Microsoft Excel文件", "*.xlsx"), (
        "Microsoft Excel 97-20003 文件", "*.xls")])
        if file_name_path == '':
            pass
        else:
            len_wid_thick_str = askstring("", prompt="请输入长度 宽度 厚度 通道1/3：mm")
        # 长宽和厚度用空格隔开，通道1表明这是通道1和2的规格，通道3表明这是通道2和3的规格。我们的焊接通道二通常为直流
            if file_name_path != '' and len_wid_thick_str is not None:
                RH_csv_advance.RH_csv_process(file_name_path, len_wid_thick_str)
                del file_name_path
                del len_wid_thick_str
            elif file_name_path != '' and len_wid_thick_str is None:
                RH_csv.RH_csv_process(file_name_path)
                del file_name_path
            else:
                pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_Plot_MH():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的dat文件", filetypes=[("dat文件", "*.dat")])
        mass_str = askfloat(title="", prompt="请输入质量：g")
        if file_name_path != '' and mass_str != '':
            Plot_MH.Plot_MH_process(file_name_path, mass_str)
            del file_name_path
            del mass_str
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_Plot_RH():
    try:
        file_name_path = askdirectory(title="请选择一个要打开的文件夹")
        if file_name_path != '':
            Plot_RH.getFileName(file_name_path)
            del file_name_path
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_DOS():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的dat文件", filetypes=[("dat文件", "*.dat")])
        if file_name_path != '':
            nedos_str = ''
            nedos_str = int(askstring("", prompt="请输入NEDOS值："))
            # tkinter.messagebox.showinfo('提示', "稍微等那么一会会儿，好吗？")
            DOS.Dos_process(file_name_path, nedos_str)
            del file_name_path, nedos_str
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_EIG():
    try:
        file_name_path = askopenfilename(title="请选择一个要打开的dat文件", filetypes=[("任意文件", "*")])
        if file_name_path != '':
            # tkinter.messagebox.showinfo('提示', "稍微等那么一会会儿，好吗？")
            EIGENVAL.Eigenval_process(file_name_path)
            del file_name_path
        else:
            pass
    except:
        tkinter.messagebox.showinfo('提示', "文件错误")


def run_help():
    tkinter.messagebox.showinfo('提示', "不要Help，我也想要Help")


win = tkinter.Tk()
win.title("工具箱")  # 添加标题
win.geometry("400x0")
# 创建菜单栏功能
menuBar = Menu(win)
win.config(menu=menuBar)
# 创建一个名为File的菜单项
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
# 在菜单项File下面添加一个名为Input的选项
fileMenu.add_command(label="Component", command=run_Component)
# 在两个菜单选项中间添加一条横线
fileMenu.add_separator()
# 在菜单项下面添加一个名为Exit的选项
fileMenu.add_command(label="Quit", command=_quit)
# 创建一个名为Calculation的菜单项
calMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Calculation", menu=calMenu)
# 在菜单项下面添加一个名为Mass的选项
calMenu.add_command(label="Mass", command=run_mass)
# 在两个菜单选项中间添加一条横线
calMenu.add_separator()
# 在菜单项下面添加一个名为Tran的选项
calMenu.add_command(label="Moment", command=run_moment)
#############################################################################################
dataMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Data", menu=dataMenu)
dataMenu.add_command(label="MH", command=run_MH)
dataMenu.add_separator()
dataMenu.add_command(label="RH", command=run_RH)
dataMenu.add_separator()
dataMenu.add_command(label="RH_csv", command=run_RH_csv)
#############################################################################################
plotMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Plot", menu=plotMenu)
plotMenu.add_command(label="MH", command=run_Plot_MH)
plotMenu.add_separator()
plotMenu.add_command(label="RH", command=run_Plot_RH)
#############################################################################################
vaspMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Vasp", menu=vaspMenu)
vaspMenu.add_command(label="DOS", command=run_DOS)
vaspMenu.add_separator()
vaspMenu.add_command(label="EIG", command=run_EIG)
#############################################################################################
# 在菜单栏中创建一个名为Help的菜单项
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
# 在菜单栏Help下添加一个名为About的选项
helpMenu.add_command(label="About", command=run_help)
win.mainloop()  # 进入主事件循环，当调用mainloop()时,窗口才会显示出来
