def Eigenval_process(eig_path):
    import tkinter.messagebox
    import getpass

    user = getpass.getuser()
    up_path = 'C:/Users/' + user + '/Desktop/EIGENVAL_UP.dat'
    dn_path = 'C:/Users/' + user + '/Desktop/EIGENVAL_DN.dat'
    write_eig_up = open(up_path, "w")
    write_eig_dn = open(dn_path, "w")
    with open(eig_path, "r") as eigenval:
        raw_content = eigenval.readlines()
    title = raw_content[0:6]
    write_eig_up.writelines(title)
    write_eig_dn.writelines(title)
    content = raw_content[7:]
    entries = []
    abstract = []
    eng_1 = []
    eng_2 = []
    for i, line in enumerate(content):
        if len(line.split()) == 4:
            entries.append(i)
            abstract.append(line)
    for k in entries:
        write_eig_up.write('\n')
        write_eig_up.writelines(abstract[entries.index(k)])
        for lines in content[k + 1:k+entries[1]-1]:
            if len(lines.split()) == 5:
                eng_1.append(lines.split()[0])
                eng_1.append(' ')
                eng_1.append(lines.split()[1])
                eng_1.append(' ')
                eng_1.append(lines.split()[3] + '\n')
                write_eig_up.writelines(eng_1)
                eng_1.clear()

            else:
                break
    for l in entries:
        write_eig_dn.write('\n')
        write_eig_dn.writelines(abstract[entries.index(l)])
        for lines in content[l + 1:l+entries[1]-1]:
            if len(lines.split()) == 5:
                eng_2.append(lines.split()[0])
                eng_2.append(' ')
                eng_2.append(lines.split()[2])
                eng_2.append(' ')
                eng_2.append(lines.split()[4] + '\n')
                write_eig_dn.writelines(eng_2)
                eng_2.clear()
            else:
                break
    write_eig_up.close()
    write_eig_dn.close()
    tkinter.messagebox.showinfo('提示', "完成！文件在桌面~~~~")
