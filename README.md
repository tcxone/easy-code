# easy-code

一个简单的编程语言，采用中文命令，使用Python编译运行

后缀名为`.ecode`

## 使用方法

下载本项目到本地后

```
cd easy-code
```

```
sh run.sh HelloWorld.ecode
```

## 语法

### 1，基本语法

```
#命令 表达式
```

### 2，输出内容

```
#输出 表达式
```

#### 示例

```
输出变量
#输出 bianliangming

输出一个字符
#输出 a

输出数字
#输出 123

输出字符串
#输出 “abc”

输出含有加号的（加号可以连接内容）
#输出 “abc” + bianliangming
```

注意必须是英文的引号

### 3，变量或计算

```
#变量 表达式
#计算 表达式
```

#### 示例

```
#计算 a = 1 + 1
#变量 abc = "string"
#变量 num = 123
```

### 4，输入

```
#输入 bianliangming（"提示内容"）
```

#### 示例

```
#输入 n（"请输入n的值"）
```

### 5，插入

```
#插入 python代码
```

#### 示例

```
#插入 print("abc")
#插入 number = 7
#插入 guess = -1
#插入 print("数字猜谜游戏!")
#插入 while guess != number:
#插入     guess = int(input("请输入你猜的数字："))
#插入     if guess == number:
#插入         print("恭喜，你猜对了！")
#插入     elif guess < number:
#插入         print("猜的数字小了...")
#插入     elif guess > number:
#插入         print("猜的数字大了...")
```