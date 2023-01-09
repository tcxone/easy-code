import re
def ecode(line):
    try:
        code = ""
        #去掉末尾的换行符
        if line.endswith('\n'):
            line = line[:-1]
        #获取操作
        #print(line)
        caozuo = re.findall(r'#(\S*)',line)
        caozuo_str = caozuo[0]

        if caozuo_str == "变量" or caozuo_str == "计算":
            code = line[4:]
        elif caozuo_str == "输出":
            code = "print(" + line[4:] + ")"
        elif caozuo_str == "输入":
            tishi = re.search(r'"([^"]*)"',line)
            tishi_str = tishi[0]
            #获取左括号的位置
            i = 0
            for sub_shuchu in line:
                if sub_shuchu == "（":
                    break
                i = i + 1
            code = line[4:i]+ " = input(" + tishi_str + ")"
        else:
            #无操作
            print("error")
        #print(code)
        with open("out.py","a") as file:
            file.write(code + "\n")
    except:
        print("error")


with open("HelloWorld.ecode") as f:
    for line in f:
        ecode(line)
print("done")