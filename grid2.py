import pygame
import cv2
import time

class Agente:
    def __init__(self, start_position):
        self.position = start_position

    def move_right(self):
        x, y = self.position
        if y + 1 < len(grid[0]) and grid[x][y + 1] != 1:
            self.position = (x, y + 1)
        time.sleep(1)
        pygame.draw.rect(screen, color, pygame.Rect(self.position[1] * 100, self.position[0] * 100, 100, 100))
        pygame.display.update()

        return self.position

    def move_left(self):
      x, y = self.position
      if y - 1 >= 0 and grid[x][y - 1] != 1:
        self.position = (x, y - 1)
      time.sleep(1)
      pygame.draw.rect(screen, color, pygame.Rect(self.position[1] * 100, self.position[0] * 100, 100, 100))
      pygame.display.update()

      return self.position

    def move_up(self):
      x, y = self.position
      if x - 1 > 0 and grid[x - 1][y] != 1:
        self.position = (x - 1, y)
      time.sleep(1)
      pygame.draw.rect(screen, color, pygame.Rect(self.position[1] * 100, self.position[0] * 100, 100, 100))
      pygame.display.update()

      return self.position

    def move_down(self):
      x, y = self.position
      if x + 1 < len(grid[0]) and grid[x + 1][y] != 1:
        self.position = (x + 1, y)
      time.sleep(1)
      pygame.draw.rect(screen, color, pygame.Rect(self.position[1] * 100, self.position[0] * 100, 100, 100))
      pygame.display.update()

      return self.position
    
    

def print_grid(grid):
    for row in grid:
        print(row)

def move_agente(num_linha, linha, agente):
  for i in range(agente.position[1], len(linha)):
    #AGENTE PARA DIREITA
    if i + 1 < len(linha) and linha[i + 1] in [0, 'G']:
      agente.move_right()
      if linha[i + 1] == 'G':
        agente.move_right()
        print('AGENTE CHEGOU AO FIM')
        return True

    #AGENTE PARA ESQUERDA
    elif i - 1 > 0 and linha[i - 1] in [0, 'G']:
      if agente.position[1] < linha[i]:
        agente.move_left()
      elif linha[i - 1] == "G":
        agente.move_left()
        print('AGENTE CHEGOU AO FIM')
        return True

    #AGENTE PARA BAIXO
    if num_linha + 1 < len(grid) and grid[num_linha + 1][agente.position[1]] in [0, 'G']:
      agente.move_down()
      if grid[num_linha + 1][agente.position[1]] == 'G':
        agente.move_down()
        print('AGENTE CHEGOU AO FIM')
        return True
      break

    #AGENTE PARA CIMA
    elif num_linha - 1 < 0 and grid[num_linha - 1][agente.position[1]] in [0, 'G']:
      agente.move_up()
      if grid[num_linha - 1][agente.position[1]] == 'G':
        agente.move_up()
        print('AGENTE CHEGOU AO FIM')
        return True
      break
    


def drawGrid(screen, white):
    blockSize = 100 
    for x in range(0, 500, blockSize):
        for y in range(0, 500, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

if __name__ == "__main__":

    grid = [
        ['S', 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 'G', 0]
    ]

    print_grid(grid)
    agente = Agente(start_position=(0, 0))
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    done = False
    color = (255, 255, 255)
    white = (200, 200, 200)
    black = (0, 0, 0)
    screen.fill(black)


    while not done:
        drawGrid(screen, white)
        time.sleep(1)
        pygame.draw.rect(screen, color, pygame.Rect(agente.position[1], agente.position[0], 100, 100))
        for i in range(0, len(grid)):
            for event in pygame.event.get():
                if event.type == "QUIT":
                    done = True
            fim = move_agente(i, grid[i], agente)
            pygame.display.update()
            if fim == True:
               time.sleep(2)
               done = True