import pygame

WIDTH = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5


base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    grid[p//side][p%side] = 0
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    i,j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i-1][j-1] != 0:
                    return
                if event.key == 48: #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 45 - buffer, 50 - buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10): #Checking for valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 45 - buffer, 50 - buffer))
                    value = myfont.render(str(event.key - 48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0,10):
        if i%3 ==0:
            pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 5)
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 5)

        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if 0<grid[i][j]<10:
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return
    
main()
