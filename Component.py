import tkinter.messagebox
import re

Relative_atomic_mass = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.017,
                            'N': 14.0067,
                            'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305,
                            'Al': 26.9815386,
                            'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983,
                            'Ca': 40.078,
                            'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                            'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723,
                            'Ge': 72.64,
                            'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62,
                            'Y': 88.90585,
                            'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 97.9072, 'Ru': 101.07, 'Rh': 102.9055,
                            'Pd': 106.42,
                            'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6,
                            'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547,
                            'Ce': 140.116,
                            'Pr': 140.90765, 'Nd': 144.242, 'Pm': 145, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                            'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                            'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23,
                            'Ir': 192.217,
                            'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                            'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254,
                            'Ac': 227.0278,
                            'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642,
                            'Am': 243.0614,
                            'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951,
                            'Md': 258.0951,
                            'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
                            'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294,
                            'Og': 294,
                            'ZERO': 0}
Input_molecular_formula = {}  # 存储元素，这是一个字典
Output_molecular_formula = []  # 输出面板
molecular_mass = 0.0


def Molecular_Weight_Calculator(molecular_formula):
    global molecular_mass
    # Input_molecular_formula = {}  # 存储元素
    if molecular_formula is not None:
        try:
            molecular_mass = 0.0  # 分子量 ， 每一次的分子量都重新定义， 否则之后会累加， 不能重复使用。
            Input_molecular_formula.clear()  # 清空列表
            molecular_formula = re.sub("[A-Z]", lambda x: "+" + x.group(0), molecular_formula)  # 大写字母前加+
            molecular_formula = re.sub("[0-9]", lambda x: "*" + x.group(0), molecular_formula)  # 数字前加*
            for character in range(len(molecular_formula)):
                molecular_formula = molecular_formula.replace("*" + str(character) + "*", "*" + str(character))
                molecular_formula = molecular_formula.replace("." + "*" + str(character), "." + str(character))
            molecular_formula_list = molecular_formula.split("+")
            # molecular_formula = [x.strip() for x in molecular_formula if x.strip() != ''] # 等价
            molecular_formula_list.pop(0)
            for character_str in molecular_formula_list:
                if "*" in character_str:
                    Input_molecular_formula[character_str.split("*")[0]] = character_str.split("*")[1]
                else:
                    Input_molecular_formula[character_str] = '1'
            # print(Input_molecular_formula)
            for dict_ele in Input_molecular_formula:
                if dict_ele not in Relative_atomic_mass:
                    tkinter.messagebox.showerror('错误', '请确保您的元素输入正确！')
                    break
                else:
                    molecular_mass += Relative_atomic_mass[dict_ele] * float(Input_molecular_formula[dict_ele])
            tkinter.messagebox.showinfo('提示', "分子量为：" + str(round(molecular_mass, 4)) + 'g/mol')
            return molecular_mass
            # return Input_molecular_formula
        except:
            tkinter.messagebox.showinfo('提示', '请输入符合要求的内容！')
    else:
        pass


def sample_mass(All_mass):
    global mass
    if All_mass is not None:
        try:
            if " " not in All_mass:
                for dict_ele in Input_molecular_formula:
                    mass = format(Relative_atomic_mass[dict_ele] * float(
                        Input_molecular_formula[dict_ele]) / molecular_mass * float(All_mass), '.7f')
                    Output_molecular_formula.append(
                        dict_ele + '      ' + str(format(Relative_atomic_mass[dict_ele], '.4f')) + '      ' + str(mass))
                tkinter.messagebox.showinfo('提示', '\n'.join(i for i in Output_molecular_formula))
                Output_molecular_formula.clear()
            elif " " in All_mass:
                try:
                    Mass = float(All_mass.split(" ")[1]) / Relative_atomic_mass[All_mass.split(" ")[0]] / float(
                        Input_molecular_formula[All_mass.split(" ")[0]]) * molecular_mass
                    for dict_ele in Input_molecular_formula:
                        if dict_ele == All_mass.split()[0]:
                            mass = format(float(All_mass.split()[1]), '.7f')
                        else:
                            mass = format(Relative_atomic_mass[dict_ele] * float(
                                Input_molecular_formula[dict_ele]) / molecular_mass * Mass, '.7f')
                        Output_molecular_formula.append(
                            dict_ele + '      ' + str(format(Relative_atomic_mass[dict_ele], '.4f')) + '      ' + str(
                                mass))
                    tkinter.messagebox.showinfo('提示', '\n'.join(i for i in Output_molecular_formula))
                    Output_molecular_formula.clear()
                except:
                    tkinter.messagebox.showerror('错误', '根据某一已知质量求其它质量出错！')
            else:
                tkinter.messagebox.showerror('错误', '典型输入错误，请按固定格式输入！')
        except:
            tkinter.messagebox.showerror('错误', '输入总质量求其它质量出错，请检查！')
    else:
        pass


def trans(magnetization, mass_g):
    if magnetization is not None and mass_g is not None:
        try:
            Mom = magnetization / mass_g * molecular_mass / 5584.8
            tkinter.messagebox.showinfo('提示', "磁矩为：" + str(round(Mom, 4)) + 'uB/f.u.')
        except:
            tkinter.messagebox.showerror('错误', '未知错误！')
    else:
        pass
