# -*- coding: UTF-8 -*-
# helloworld.py

# 导入需要的模块
import pygame, sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((640, 480))

# 设置窗口的标题
pygame.display.set_caption('Hello World! I am Miyoo Mini')

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

# 通过字体文件获得字体对象（可以自己下载一个字体包实验看看）
fontObj = pygame.font.Font('assets/simhei.ttf', 25)

# 配置要显示的文字
text = ''
textSurfaceObj = fontObj.render('- Hello World !', True, BLACK, WHITE)
# 获得要显示的对象的rect
textRectObj = textSurfaceObj.get_rect()
# 设置显示对象的坐标
textRectObj.center = (150, 125)

textSurfaceObj2 = fontObj.render('- 我是 Miyoo Mini', True, BLACK, WHITE)
# 获得要显示的对象的rect
textRectObj2 = textSurfaceObj2.get_rect()
# 设置显示对象的坐标
textRectObj2.center = (150, 175)

# 设置背景
screen.fill(WHITE)

# 绘制字体
screen.blit(textSurfaceObj, textRectObj)
screen.blit(textSurfaceObj2, textRectObj2)


def main():
    # 程序主循环
    while True:
        # 获取事件
        for event in pygame.event.get():
            # 判断事件是否为退出事件
            if event.type == pygame.K_ESCAPE:
                # 退出pygame
                pygame.quit()
                # 退出系统
                sys.exit()

        # 绘制屏幕内容
        pygame.display.update()


if __name__ == "__main__":
    main()
