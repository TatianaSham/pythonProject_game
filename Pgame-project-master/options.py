import pygame
import button


def optionss():
  pygame.init()

  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Правила игры")

  pygame.font.init()
  options_img = pygame.image.load("menu.png").convert_alpha()
  options_button = button.Button(450, 500, options_img, 1)
  def load_image(name, colorkey=None):
      fullname = pygame.image.load(name)
      return fullname

  sprite = pygame.sprite.Sprite()
  sprite.image = load_image("arrow1.png")
  sprite.rect = sprite.image.get_rect()
  all_sprites = pygame.sprite.Group(sprite)

  text = "Уровень 1:\n" \
         "- Кружки начинают двигаться от верхней части экрана вниз по четырем вертикальным полосам.\n" \
         "- Игрок должен нажать соответствующую клавишу на клавиатуре, когда кружок достигает определенного уровня.\n" \
         "- Клавиша D - красный кружок, F - зеленый, K - синий, L - желтый, соответственно.\n" \
         "- За каждое правильное нажатие игрок получает 25 очков.\n" \
         "Уровень 2:\n" \
         "- Скорость движения кружков увеличивается, усложняя игру.\n" \
         "- Теперь игрок должен быстрее реагировать, чтобы нажать правильную клавишу вовремя.\n" \
         "- За каждое правильное нажатие игрок получает 10 очков.\n" \
         "Уровень 3:\n" \
         "- Кружки двигаются еще быстрее, и игрок должен быть очень внимателен, чтобы успеть нажать правильную клавишу.\n" \
         "- За каждое правильное нажатие игрок получает 5 очков.\n" \
         "\n" \
         "Цель игры - набрать как можно больше очков. Максимальное количество очков - 1000" \
         "\n" \
         "D - отвечает за первую полосу \n" \
         "F - отвечает за вторую полосу \n" \
         "K - отвечает за третью полосу \n" \
         "L - отвечает за четвёртую полосу"
  font = pygame.font.SysFont('Arial', 22)


  def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


  run = True
  while run:
    screen.fill((12, 48, 90))
    blit_text(screen, text, (20, 20), font)


    if options_button.draw(screen):
        menu1()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEMOTION:
        sprite.rect.x = event.pos[0]
        sprite.rect.y = event.pos[1]
    if pygame.mouse.get_focused():
      pygame.mouse.set_visible(False)
      all_sprites.draw(screen)
    pygame.display.update()

  pygame.quit()

def menu1():
    from main import main
    main()
