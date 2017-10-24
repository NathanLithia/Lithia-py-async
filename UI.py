import pygame
pygame.init()

display_width = 1366
display_height = 768
Background = (12,12,12)
LithiaIMG = pygame.image.load('Lithiatpa.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Lithia')
clock = pygame.time.Clock()

def Lithia(x,y):
  gameDisplay.blit(LithiaIMG, (x,y))
x = ((display_width / 2) - (LithiaIMG.get_height() / 2))
y = ((display_height / 2) - (LithiaIMG.get_height() / 2))
crashed = False

while not crashed:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True
    print(event)
  gameDisplay.fill(Background)
  Lithia(x,y)
  pygame.display.update()
  clock.tick(60)
pygame.quit()
quit()