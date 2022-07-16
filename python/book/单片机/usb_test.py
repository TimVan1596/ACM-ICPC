import serial  # pip install pyserial
import chardet  # 如果你decode()不知道什么编码格式，可以用这个包

# chardet.detect(bytes_data)  # 查看串口返回来的数据到底是什么编码！


'''
COM3为端口

962100为比特率（Baudrate），填的数字要求大于等于硬件设备的比特率，不然decode()会报错，
或者不是自己想要的数据

timeout 设置超时
'''

if __name__ == '__main__':
    ser = serial.Serial('COM1', 19200, timeout=0.5)

    a = ser.read_until(expected=b'\n')  # 读取一帧数据 ，读到\n为止。
    # 你也可以read_line啥的，因为发送过来的一帧数据可能太长，会读取不完整，所以一条数据读到\n这里正好。

    a.decode()  # 很多人会在这里报错，或者得到的解析数据不是自己想要的结果，
    # 是因为比特率设置的频率小于硬件设备的比特率，你可以随便设置一个很大的数字即可成功

    print(a)

    ser.close()  # 关闭端口
