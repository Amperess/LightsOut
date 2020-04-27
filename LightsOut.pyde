from functools import reduce

onOutline = color(245, 197, 66)
onFill = color(245, 233, 66)
offOutline = color(0, 0, 0)
offFill = color(167, 167, 167)

currRound = 6
roundPos = [
            [ [50,50], [150,150] ], 
            [ [50, 200], [100, 200], [150, 200] ],
            [ [50, 200], [100, 200], [150, 200], [200, 200] ],
            [ [50, 200], [100, 200], [150, 200], [200, 200], [250, 200] ],
            [ [100, 100], [300, 100], [100, 200], [300, 200] ],
            [ [100, 100], [300, 100], [100, 200], [300, 200], [400, 200] ],
            [ [150, 150], [250, 100], [350, 150], [250, 200], [150, 200], [250, 150], [350, 200], [250, 250] ],
            [ [50, 75], [125, 100], [200, 200], [250, 200], [325, 100], [400, 75], [50, 325], [125, 300], [325, 300], [400, 325] ]
            ]
roundLights = [[False]*len(i) for i in roundPos]
roundEdges = [ 
              [ [0,1] ],
              [ [0,1], [1,2] ],
              [ [0,1], [1,2], [2, 3] ],
              [ [0,1], [1,2], [2, 3], [3, 4] ],
              [ [0,1], [0,2], [2,3], [1,3] ],
              [ [0,1], [0,2], [2,3], [1,3], [3,4] ],
              [ [0,1], [1,2], [2,3], [0,3], [0,4], [1,5], [2,6], [3,7], [4,5], [5,6], [6,7], [4,7] ],
              [ [0,1], [1,2], [2,3], [4,5], [6,7], [7,2], [3,8], [8,9], [1,7], [4,8], [3,4] ]
              ]
circleRadius = 30

firstLoop = True
startFrameCount = -160


def setup():
    size(500, 500)

def draw():
    drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound])
    checkWin()


def checkWin():
    global currRound, firstLoop, startFrameCount
    win = reduce((lambda x, y: x and y), roundLights[currRound])
    if win:
        if firstLoop:
            startFrameCount = frameCount
            firstLoop = False
        if frameCount > startFrameCount + 100:
            if currRound+1 < len(roundPos):
                currRound += 1
                firstLoop = True
        if frameCount > startFrameCount + 60:
            if currRound+1 == len(roundPos):
                drawTextScreen("Game complete!")
            else:
                drawTextScreen("Round " + str(currRound+1) + " complete!")

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
        drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound])
    
    
def checkPos(x, y):
    for i in range(0, len(roundPos[currRound])):
        if sqrt((x-roundPos[currRound][i][0])**2 + (y-roundPos[currRound][i][1])**2) < circleRadius:
            return i
    return -1
            
