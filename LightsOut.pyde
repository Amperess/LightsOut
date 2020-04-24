onOutline = color(245, 197, 66)
onFill = color(245, 233, 66)
offOutline = color(0, 0, 0)
offFill = color(167, 167, 167)

roundPos = [[[50,50], [150,150]]]
roundLights = [[True, True]]
roundEdges = [[[0,1]]]
currRound = 0
circleRadius = 30

def setup():
    size(500, 500)

def draw():
  drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound])


'''
Draw the graph with yellow circle at posArr[i] where lightOnArr[i] is True
'''
def drawGraph(posArr, lightOnArr, edgesArr):
  
  stroke(color(0,0,0))
  for edge in edgesArr:
    startX = posArr[edge[0]][0]
    startY = posArr[edge[0]][1]
    endX = posArr[edge[1]][0]
    endY = posArr[edge[1]][1]
    line(startX, startY, endX, endY);

  for i in range(0, len(posArr)):
      if lightOnArr[i]:
        stroke(onOutline)
        fill(onFill)
      else:
        stroke(offOutline)
        fill(offFill)
        
      circle(posArr[i][0], posArr[i][1], circleRadius)

def mouseClicked():
    within = checkPos(mouseX, mouseY)
    if within != -1:
        roundLights[currRound][within] = not roundLights[currRound][within]
        print(roundLights[currRound])
    
    
def checkPos(x, y):
    for i in range(0, len(roundPos[currRound])):
        if sqrt((x-roundPos[currRound][i][0])**2 + (y-roundPos[currRound][i][1])**2) < circleRadius:
            return i
    return -1
            
