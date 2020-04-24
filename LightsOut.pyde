from functools import reduce

onOutline = color(245, 197, 66)
onFill = color(245, 233, 66)
offOutline = color(0, 0, 0)
offFill = color(167, 167, 167)

currRound = 0
roundPos = [[ [50,50], [150,150] ], [ [50, 50], [150, 150], [300, 150] ]]
roundLights = [[False, False], [False, False, False]]
roundEdges = [ [ [0,1]  ], [ [0,1], [1,2] ] ]
circleRadius = 30

firstLoop = True


def setup():
    size(500, 500)

def draw():
  drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound])
  checkWin()


def checkWin():
    global currRound, firstLoop
    startFrameCount = -160
    win = reduce((lambda x, y: x and y), roundLights[currRound])
    if win:
        if currRound+1 == len(roundPos):
            drawTextScreen("Game complete!")
        else:
            drawTextScreen("Round " + str(currRound+1) + " complete!")
        if firstLoop:
            startFrameCount = frameCount
            firstLoop = False
        if frameCount > startFrameCount + 300:
            if currRound+1 < len(roundPos):
                currRound += 1
                firstLoop = True

'''
Draw the graph with yellow circle at posArr[i] where lightOnArr[i] is True
'''
def drawGraph(posArr, lightOffArr, edgesArr):
  background(color(200, 200, 200))
  
  stroke(color(0,0,0))
  for edge in edgesArr:
    startX = posArr[edge[0]][0]
    startY = posArr[edge[0]][1]
    endX = posArr[edge[1]][0]
    endY = posArr[edge[1]][1]
    line(startX, startY, endX, endY);

  for i in range(0, len(posArr)):
      if lightOffArr[i]:
        stroke(offOutline)
        fill(offFill)
      else:
        stroke(onOutline)
        fill(onFill)
        
      circle(posArr[i][0], posArr[i][1], circleRadius)

def drawTextScreen(textStr):
    background(color(64, 235, 52));
    textSize(32);
    fill(255, 255, 255);
    text(textStr, 100, 250);

def mouseClicked():
    within = checkPos(mouseX, mouseY)
    if within != -1:
        roundLights[currRound][within] = not roundLights[currRound][within]
        for edge in roundEdges[currRound]:
            if edge[0] == within:
                roundLights[currRound][edge[1]] = not roundLights[currRound][edge[1]]
            elif edge[1] == within:
                roundLights[currRound][edge[0]] = not roundLights[currRound][edge[0]]
        print(roundLights[currRound])
    
    
def checkPos(x, y):
    for i in range(0, len(roundPos[currRound])):
        if sqrt((x-roundPos[currRound][i][0])**2 + (y-roundPos[currRound][i][1])**2) < circleRadius:
            return i
    return -1
            
