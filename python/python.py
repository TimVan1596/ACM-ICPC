# -*- coding: UTF-8 -*-
# helloworld.py
 
# 导入所需的模块
import pygame, sys
# 导入所有pygame.locals里的变量（比如下面大写的QUIT变量）
from pygame.locals import *
 
 
# 初始化pygame
pygame.init()
 
# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((320, 240))
 
# 设置窗口标题
pygame.display.set_caption('Hello World! I am Miyoo Mini')
 
# 程序主循环
while True:
 
  # 获取事件
  for event in pygame.event.get():
    # 判断事件是否为退出事件
    if event.type == QUIT:
      # 退出pygame
      pygame.quit()
      # 退出系统
      sys.exit()
 
  # 绘制屏幕内容
  pygame.display.update()
