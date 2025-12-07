import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    print(f"(!) Pygame 初始化失败... 错误数: {check_errors[1]}")
    sys.exit(-1)
else:
    print("(+) Pygame 初始化成功!")

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('贪吃蛇 by AI')

fps_controller = pygame.time.Clock()
GAME_SPEED = 15  # 蛇的移动速度，数值越大越快

snake_pos = [100, 50]  # 蛇头的初始位置
# 蛇的身体，由多个方块组成
snake_body = [[100, 50], [90, 50], [80, 50]]
SNAKE_BLOCK_SIZE = 10  # 蛇和食物方块的大小

direction = 'RIGHT'
change_to = direction

food_pos = [random.randrange(1, (SCREEN_WIDTH // SNAKE_BLOCK_SIZE)) * SNAKE_BLOCK_SIZE,
            random.randrange(1, (SCREEN_HEIGHT // SNAKE_BLOCK_SIZE)) * SNAKE_BLOCK_SIZE]
food_spawn = True

# 分数
score = 0

def show_score(choice, color, font, size):
    """在屏幕上显示分数"""
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (SCREEN_WIDTH / 10, 15)
    else:
        score_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.25)
    screen.blit(score_surface, score_rect)


def game_over():
    """游戏结束处理"""
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    show_score(0, RED, 'times', 20)
    pygame.display.flip()  # 更新屏幕显示"YOU DIED"
    time.sleep(2)  # 等待2秒
    pygame.quit()  # 退出pygame
    sys.exit()  # 退出程序


# 4. 游戏主循环
# ---------------------------------------------------

while True:
    # --- 事件处理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 监听键盘按键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # 按下 ESC 键退出游戏
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # --- 更新蛇的方向 ---
    # 防止蛇直接掉头（例如，从右直接到左）
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # --- 更新蛇头的位置 ---
    if direction == 'UP':
        snake_pos[1] -= SNAKE_BLOCK_SIZE
    if direction == 'DOWN':
        snake_pos[1] += SNAKE_BLOCK_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= SNAKE_BLOCK_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += SNAKE_BLOCK_SIZE

    # --- 蛇的身体增长机制 ---
    # 将新的蛇头位置插入到身体列表的最前面
    snake_body.insert(0, list(snake_pos))
    # 检查是否吃到食物
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False  # 食物被吃了，需要重新生成
    else:
        # 如果没吃到食物，就移除蛇尾，保持身体长度不变，造成移动的假象
        snake_body.pop()

    # --- 食物生成 ---
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // SNAKE_BLOCK_SIZE)) * SNAKE_BLOCK_SIZE,
                    random.randrange(1, (SCREEN_HEIGHT // SNAKE_BLOCK_SIZE)) * SNAKE_BLOCK_SIZE]
    food_spawn = True

    # --- 绘制游戏元素 ---
    # 填充背景色
    screen.fill(BLACK)

    # 绘制蛇
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE))

    # 绘制食物
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE))

    # --- 游戏结束条件判断 ---
    # 1. 撞到墙壁
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - SNAKE_BLOCK_SIZE:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - SNAKE_BLOCK_SIZE:
        game_over()

    # 2. 撞到自己身体
    # 遍历蛇身体的每一块（除了蛇头）
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # --- 刷新屏幕 ---
    show_score(1, WHITE, 'consolas', 20)
    pygame.display.update()

    # --- 控制游戏速度 ---
    fps_controller.tick(GAME_SPEED)