import argparse  # 一种通过终端交互的方式
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--hight', type=int, default=10, help='这是个高度')
parser.add_argument('-w', '--weight', type=int, default=12, help='这是宽度')
arg = parser.parse_args()   # 解析所有参数
print(arg.hight)
print(arg.weight)
import os
pth = r'D:\Data\PHM2009gearbox\PHM_Society_2009_Competition_Expanded_txt'
for x in os.listdir(pth):
    for y in os.listdir(os.path.join(pth, x)):
        if y.endswith('.zip'):
            os.remove(os.path.join(pth, x, y))