# -*-coding:UTF-8-*-

with open('静夜思.txt', 'w') as File:
    File.write('静夜思\n窗前明月关，\n 疑是地上霜.\n')

with open('静夜思.txt', 'r') as File:
    for line in File.readlines():
        print(line)

