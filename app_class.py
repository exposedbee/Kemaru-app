import pygame, sys, random, time
from settings import *
from buttonClass import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.grid = []
        self.finishedBoard = []
        self.boardShapes = []
        #print(self.grid)
        self.selected = None
        self.mousePos = None
        self.state = "start"
        self.begin = 0
        self.end = 0
        self.elapsed = 0
        self.timer = False
        self.timerText = ""
        self.totalGameCount= 0
        self.winText = ''
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.finished = False
        self.gameMode = 0
        self.endButton = []
        self.lockedCells = []
        self.cellChanged = False
        self.incorrectCells = []
        self.hint = False
        self.hintSelect = False
        self.changed = False
        self.solution = False
        self.font = pygame.font.SysFont("arial", int(cellSize[self.gameMode])//2)
        self.load()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()

            if self.state == "start":
                self.start_events()
                self.start_update()
                self.start_draw()

            if self.state == "finished":
                self.finished_events()
                self.finished_update()
                self.finished_draw()
        pygame.quit()
        sys.exit
##Start start_events
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'start'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mousePos[0] > 150 and self.mousePos[1] > 300 and self.mousePos[0]<(150+s1) and self.mousePos[1]<(300+s2):
                    #self.state = 'playing'
                    self.gameMode = 1
                    self.hint = True
                    #print("player in")
                    self.setGame()

                elif self.mousePos[0] > 250 and self.mousePos[1] > 300 and self.mousePos[0]<(250+s1) and self.mousePos[1]<(300+s2):
                    #print('med')
                    self.hint = True
                    self.gameMode = 0
                    self.setGame()

                elif self.mousePos[0] > 350 and self.mousePos[1] > 300 and self.mousePos[0]<(350+s1) and self.mousePos[1]<(300+s2):
                    #print('hard')
                    self.hint = False
                    self.gameMode = 0
                    self.setGame()
                elif self.mousePos[0] > 250 and self.mousePos[1] > 450 and self.mousePos[0]<(250+s1) and self.mousePos[1]<(450+s2):
                    pygame.quit()
                    sys.exit



    def start_draw(self):
        self.window.fill(WHITE)
        self.start_draw_text('Kemaru',self.window, STARTTEXTSIZE, COLORSTART)
        for button in self.menuButtons:
            button.draw(self.window)
        pygame.display.update()

    def start_draw_text(self, word, window, size, colour):
        font = pygame.font.SysFont("bahnschrift", size)
        text = font.render(word, False, colour)

        self.window.blit(text, (230,200))
    def start_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.menuButtons:
            button.update(self.mousePos)



##start menu end
## Playing state functions

    def playing_events(self):
        self.end = time.time()
        self.elapsed = int(self.end-self.begin)
        min = int(self.elapsed/60)
        sec = self.elapsed%60
        self.timerText= ""+str(min)+":"+str(sec)+"s"
        self.playingButtons.append(Button(480, 40, 100, 40,self.timerText))
        self.playingButtons.append(Button(250, 40, 100, 40, 'Back'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


                #mouse action by user
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected

                else:
                    #hint toggeling
                    if self.mousePos[0] > 20 and self.mousePos[1] > 40 and self.mousePos[0]<(20+s1) and self.mousePos[1]<(40+s2) and self.hint:
                        #print('hint selected')
                        self.hintSelect= not self.hintSelect
                        if self.hintSelect:
                            self.playingButtons.append(Button(20, 40, 100, 40, 'Hint', (255,0,0),(255,99,71)))
                        else:
                            self.playingButtons.append(Button(20, 40, 100, 40, 'Hint',(0,191,255),(96,216,232)))

                    if self.mousePos[0] > 250 and self.mousePos[1] > 40 and self.mousePos[0]<(250+s1) and self.mousePos[1]<(40+s2):
                        #print("backbutton")
                        self.begin = 0
                        self.end = 0
                        if self.gameMode == 1 and self.changed and self.cellChanged != True:
                            mod1.append(self.totalGameCount)
                            #print(mod1)
                        elif self.gameMode == 0 and self.changed and self.cellChanged != True:
                            mod2.append(self.totalGameCount)
                        #print("when back",mod2)
                        self.state = 'start'
                        self.load()

                    self.selected = None
            # user input
            if event.type == pygame.KEYDOWN:
                #print(event.unicode)
                if self.selected != None and list(self.selected) not in self.lockedCells:
                    if self.isInt(event.unicode) and int(event.unicode) < 6:
                        #cell is chnaged here (check if game finished)
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellChanged = True
                        self.changed = False


    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)
        #checking if board is completed correctly (on every cell change)
        if self.cellChanged:
            self.incorrectCells = []
            for y in range(len(self.boardShapes)):
                if self.allCellsDone(y):
                    self.checkAllCells(y)

            if self.grid == self.finishedBoard:
                #print("completed")
                self.state = 'finished'
                self.finished_events()
                self.finished_update()
                self.finished_draw()
                self.load()

    def playing_draw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelected(self.window, self.selected)

        self.shadeLockedCells(self.window, self.lockedCells)
        #easy mode check
        if self.hint and self.hintSelect:
            self.shadeIncorrectCells(self.window, self.incorrectCells)

        self.drawNumbers(self.window)

        self.drawGrid(self.window)
        pygame.display.update()
        self.cellChanged = False
## Board Check functions:
    def allCellsDone(self, index):
        count = len(self.boardShapes[index])
        count2 = 0
        for z in self.boardShapes[index]:
            yCod=z%10;
            xCod=int(z/10);
            if self.grid[yCod][xCod] != 0:
                count2 = count2+1
        if count2 == count:
            #print("count true for index",index)
            return True
        return False

    def checkAllCells(self, index):
        self.checkBoxes(index)

    def checkBoxes(self, index):
        count = len(self.boardShapes[index])
        count2 = 0
        for z in self.boardShapes[index]:
            yCod=z%10;
            xCod=int(z/10);
            if self.grid[yCod][xCod] ==  self.finishedBoard[yCod][xCod]:
                count2 = count2+1
            else:
                if [xCod,yCod] not in self.lockedCells:
                    self.incorrectCells.append([xCod, yCod])
                    #print(self.incorrectCells)
        #if count == count2:
        #    print(index)
## Helper functions(selection on grid):
    def drawNumbers(self, window):
        for yi, row in enumerate(self.grid):
            for xi, num in enumerate(row):
                if num !=0:
                    pos = [(xi*int(cellSize[self.gameMode]))+gridPos[0], (yi*int(cellSize[self.gameMode]))+gridPos[1]]
                    self.textToScreen(window, str(num), pos)


    def shadeIncorrectCells(self, window, incorrect):
        for cell in incorrect:
            pygame.draw.rect(window, INCORRECTCELLCOLOUR, (cell[0]*int(cellSize[self.gameMode])+gridPos[0],cell[1]*int(cellSize[self.gameMode])+gridPos[1], int(cellSize[self.gameMode]), int(cellSize[self.gameMode])))

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, LOCKEDCELLCOLOUR, (cell[0]*int(cellSize[self.gameMode])+gridPos[0],cell[1]*int(cellSize[self.gameMode])+gridPos[1], int(cellSize[self.gameMode]), int(cellSize[self.gameMode])))
#draw(for user selected)
    def drawSelected(self, window, pos):
        pygame.draw.rect(window, LIGHTBLUE, ((pos[0]*int(cellSize[self.gameMode]))+gridPos[0], (pos[1]*int(cellSize[self.gameMode]))+gridPos[1], int(cellSize[self.gameMode]), int(cellSize[self.gameMode])))
#Draw grid
    def drawGrid(self, window):
        #pygame.draw.rect(window, DARKBLUE, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 3)
        if self.gameMode == 1:
            value =6
        else:
            value = 9
        for x in range(value):
        #initial grid outline
            pygame.draw.line(window, LIGHTGRAY, (gridPos[0]+(x*int(cellSize[self.gameMode])), gridPos[1]), (gridPos[0]+(x*int(cellSize[self.gameMode])), gridPos[1]+450))
            pygame.draw.line(window, LIGHTGRAY, (gridPos[0], gridPos[1]+(x*int(cellSize[self.gameMode]))), (gridPos[0]+450, gridPos[1]+(x*int(cellSize[self.gameMode]))))
        # print(len(self.boardShapes))
        #TODO: grid coloring code here.
        pygame.draw.rect(window, DARKBLUE, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 3)

        for y in range(len(self.boardShapes)):
                for z in self.boardShapes[y]:
                    yCod=z%10;
                    xCod=int(z/10);
                    if z+10 not in self.boardShapes[y]:
                        pygame.draw.line(window, DARKBLUE, (gridPos[0]+((xCod*int(val[self.gameMode]))+1*int(cellSize[self.gameMode])), gridPos[1]+(yCod*int(val[self.gameMode]))), (gridPos[0]+((xCod*int(val[self.gameMode]))+1*int(cellSize[self.gameMode])), gridPos[1]+((yCod*int(val[self.gameMode]))+int(val[self.gameMode]))),3)
                    if z+1 not in self.boardShapes[y]:
                        pygame.draw.line(window, DARKBLUE, (gridPos[0]+(xCod*int(val[self.gameMode])),(gridPos[1]+(yCod*int(val[self.gameMode]))+1*int(cellSize[self.gameMode]))), ((gridPos[0]+((xCod*int(val[self.gameMode]))+int(val[self.gameMode]))), (gridPos[1]+(yCod*int(val[self.gameMode]))+1*int(cellSize[self.gameMode]))),3)



#Mouse position on grid or # NOTE:
    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False

        if self.mousePos[0] > gridPos[0]+gridSize or self.mousePos[1] > gridPos[1]+gridSize:
             return False
        return ((self.mousePos[0]-gridPos[0])//int(cellSize[self.gameMode]), (self.mousePos[1]-gridPos[1])//int(cellSize[self.gameMode]))


##Button functions

    def loadButtons(self):
        if self.hint:
            self.playingButtons.append(Button(20, 40, 100, 40, 'Hint'))




    def loadButtonsStart(self):
        self.menuButtons.append(Button(150, 300, 100, 40,"EASY"))
        self.menuButtons.append(Button(250, 300, 100, 40, "MEDIUM"))
        self.menuButtons.append(Button(350, 300, 100, 40,"HARD", (135,206,135),(255,69,0)))
        self.menuButtons.append(Button(250, 450, 100, 40, "Quit"))

    def loadButtonsFinished(self):
        self.endButtons.append(Button(150, 300, 100, 40,"Play Again"))
        self.endButtons.append(Button(300, 300, 100, 40, "Solution"))
        self.endButtons.append(Button(230, 400, 100, 40, "Quit"))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (int(cellSize[self.gameMode])-fontWidth)//2
        pos[1] += (int(cellSize[self.gameMode])-fontHeight)//2
        window.blit(font,pos)

    def load(self):
        if self.state == "playing":
            self.loadButtons()
            for yi, row in enumerate(self.grid):
                for xi, num in enumerate(row):
                    if num != 0:
                        self.lockedCells.append([xi, yi])
        elif self.state == "start":
            self.loadButtonsStart()
        elif self.state == "finished":
            self.loadButtonsFinished()
        #Locked cells from original board so they cant be changed



    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False

##FINISHED GAME_events
    def finished_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mousePos[0] > 150 and self.mousePos[1] > 300 and self.mousePos[0]<(150+s1) and self.mousePos[1]<(300+s2):
                    #self.state = 'playing'
                    self.state = 'start'
                    self.load()
                elif self.mousePos[0] > 300 and self.mousePos[1] > 300 and self.mousePos[0]<(300+s1) and self.mousePos[1]<(300+s2):
                    #print("solution clicked")
                    self.solution = True
                    self.state = 'playing'
                    self.load()

                elif self.mousePos[0] > 230 and self.mousePos[1] > 400 and self.mousePos[0]<(230+s1) and self.mousePos[1]<(400+s2):
                    pygame.quit()



    def finished_draw(self):
        self.window.fill(WHITE)
        if self.timer:
            self.end = time.time()
            self.elapsed = int(self.end-self.begin)
            self.winText= "Congrulations you took: "+self.timerText
            self.timer = False

        self.finished_draw_text(self.winText,self.window, FINISHTEXTSIZE, COLORSTART)
        for button in self.endButtons:
            button.draw(self.window)
        pygame.display.update()

    def finished_draw_text(self, word, window, size, colour):
        font = pygame.font.SysFont("bahnschrift", size)
        text = font.render(word, False, colour)

        self.window.blit(text, (150,200))

    def finished_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.endButtons:
            button.update(self.mousePos)

    def setGame(self):
        if self.gameMode == 1 and len(mod1) >=1:
            self.totalGameCount= mod1.pop(random.randint(0,len(mod1)-1))
            #print(self.totalGameCount)
            if self.totalGameCount == 1:
                self.grid = testBoard1
                self.finishedBoard = finishedBoard1
                self.boardShapes = testshape1
            elif self.totalGameCount ==2:
                self.grid = testBoard2
                self.finishedBoard = finishedBoard2
                self.boardShapes = testshape2
            elif self.totalGameCount == 3:
                self.grid = testBoard3
                self.finishedBoard = finishedBoard3
                self.boardShapes = testshape3
            elif self.totalGameCount == 4:
                self.grid = testBoard4
                self.finishedBoard = finishedBoard4
                self.boardShapes = testshape4
            elif self.totalGameCount == 5:
                self.grid = testBoard5
                self.finishedBoard = finishedBoard5
                self.boardShapes = testshape5
            elif self.totalGameCount == 6:
                self.grid = testBoard6
                self.finishedBoard = finishedBoard6
                self.boardShapes = testshape6

            self.state = 'playing'
            self.timer = True
            self.changed = True
            self.begin=time.time()
            self.lockedCells.clear()
            self.load()
        elif self.gameMode == 0 and len(mod2) >=1:
            self.totalGameCount= mod2.pop(random.randint(0,len(mod2)-1))
            #print(self.totalGameCount)
            if self.totalGameCount == 1:
                self.grid = hardBoard1
                self.finishedBoard = hardfinishedBoard1
                self.boardShapes = hardshape1
            elif self.totalGameCount == 2:
                self.grid = hardBoard2
                self.finishedBoard = hardfinishedBoard2
                self.boardShapes = hardshape2
            elif self.totalGameCount == 3:
                self.grid = hardBoard3
                self.finishedBoard = hardfinishedBoard3
                self.boardShapes = hardshape3
            elif self.totalGameCount == 4:
                self.grid = hardBoard4
                self.finishedBoard = hardfinishedBoard4
                self.boardShapes = hardshape4
            self.state = 'playing'
            self.timer = True
            self.changed = True
            self.begin=time.time()
            self.lockedCells.clear()
            self.load()
