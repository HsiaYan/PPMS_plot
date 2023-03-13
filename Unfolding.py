import tkinter.messagebox
import getpass

user = getpass.getuser()
band_path = r'C:\Users\HsiaYan\Desktop\反折叠\Mn0.25\EBS_UP.dat'
EBS_up = 'C:/Users/' + user + '/Desktop/EBS_UP.dat'
write_up = open(EBS_up, "w")
with open(band_path, "r") as unfolding:
    band_content = unfolding.readlines()
#title = raw_content[0:6]
kpath = []  # 存 0，113，226，339
kpath_value = [] #　存　Kpath所在的行内容
band_value = []
for i, line in enumerate(band_content):
    if len(line.split()) == 2:
        kpath.append(i)
        kpath_value.append(line)
    if len(line.split()) == 3:
        band_value.append(line)
# print(len(band_value))
# print(len(kpath))
num =kpath[1]-kpath[0]-1
# print(num)
for k in range(num):
    write_up.write('\n')
    # print(type(kpath_value[kpath.index(k)]))
    # write_up.writelines(kpath_value[k]) 待考虑
    for l in kpath:
        # print(l)
        write_up.writelines(band_value[l+k-kpath.index(l)])
write_up.close()
