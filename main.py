import re
import sys
def ecode(line,l):
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
            print("ERROR : (line " + str(l) + ") : 未知操作")
        #print(code)
        with open("out.py","a") as file:
            file.write(code + "\n")
    except:
        print("ERROR (line " + str(l) + ") : 未知错误")


with open(sys.argv[1]) as f:
    l = 1
    for line in f:
        ecode(line,l)
        l = l + 1
print("done")