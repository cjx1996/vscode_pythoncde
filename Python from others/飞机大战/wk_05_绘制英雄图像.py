import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2. blit 绘制图像
screen.blit(bg, (0, 0))
# 3. update 更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()
