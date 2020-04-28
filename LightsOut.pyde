from functools import reduce

# Colors for off and on lights
onOutline = color(245, 197, 66)
onFill = color(245, 233, 66)
offOutline = color(0, 0, 0)
offFill = color(167, 167, 167)

greenColor = color(64, 235, 52)
redColor = color(235, 7, 15)
switchColor = greenColor

# What round is the player currently on
currRound = 0

# The positions of each light for each round
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

# Whether the light is on or off in the current round
roundLights = [[False]*len(i) for i in roundPos]

# Whether the light switch has been hit at this light in the current round
roundSwitches = [[False]*len(i) for i in roundPos]

roundMinSwitches = [1, 1, 2, 2, 4, 2, 2, 5]

# Which nodes have edges between them for each round
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

# How big to draw the lights
circleRadius = 30

# Delay information for drawing text screens
firstLoop = True
startFrameCount = -160

# Make the canvas 500 x 500 pixels
def setup():
    size(500, 500)

# Every round, draw the current round graph and the text screen on top in case they've won
def draw():
    drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound], roundSwitches[currRound])
    checkWin()

# Check if the player has turned all the lights off in the current round
def checkWin():
    global currRound, firstLoop, startFrameCount
    
    # If the light is True, it is off. Check if all lights are True
    win = reduce((lambda x, y: x and y), roundLights[currRound], roundSwitches[currRound]) and roundSwitches[currRound].count(True) <= roundMinSwitches[currRound]
    
    # Check the frame in which they win, then delay a bit, show win screen, delay a bit and move to the next stage
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


# Draw the graph with circles at posArr, colored by lightsOffArr and connected by the edgesArr
def drawGraph(posArr, lightOffArr, edgesArr, switchesArr):
  # Color the background gray
  background(color(200, 200, 200))
  
  # Draw reset button
  fill(color(247, 190, 192))
  stroke(color(0, 0, 0))
  rect(430, 0, 70, 50)
  fill(color(0, 0, 0))
  textSize(20)
  text("Reset", 440, 30)
  
  # Draw edges in black
  stroke(color(0,0,0))
  for edge in edgesArr:
    startX = posArr[edge[0]][0]
    startY = posArr[edge[0]][1]
    endX = posArr[edge[1]][0]
    endY = posArr[edge[1]][1]
    line(startX, startY, endX, endY);

  # Change switch outline color if they've exceeded the amound of switches allowed
  if roundSwitches[currRound].count(True) <= roundMinSwitches[currRound]:
      switchColor = greenColor
  else:
      switchColor = redColor

  # Draw the lights in the on or off color, with switch color if they were clicked on, otherwise default color
  for i in range(0, len(posArr)):
      if lightOffArr[i]:
          if switchesArr[i] == True:
            stroke(switchColor)
          else:
            stroke(offOutline)
          fill(offFill)
      else:
        if switchesArr[i] == True:
            stroke(switchColor)
        else:
            stroke(onOutline)
        fill(onFill)
      circle(posArr[i][0], posArr[i][1], circleRadius)

# Draw a green colored screen with the parameter textStr displayed
def drawTextScreen(textStr):
    background(color(64, 235, 52))
    textSize(32)
    fill(255, 255, 255)
    text(textStr, 110, 250)

# Handle mouse click event
def mouseClicked():
    
    if mouseX >= 430 and mouseY < 30:
        reset(currRound)
    else:
        #Check which node they clicked on
        within = checkPos(mouseX, mouseY)
        
        # If they clicked on a legal node
        if within != -1:
            # Turn that light to it's opposite value and all lights it's connected to by an edge, only switch the selected switch
            roundLights[currRound][within] = not roundLights[currRound][within]
            roundSwitches[currRound][within] = not roundSwitches[currRound][within]
            for edge in roundEdges[currRound]:
                if edge[0] == within:
                    roundLights[currRound][edge[1]] = not roundLights[currRound][edge[1]]
                elif edge[1] == within:
                    roundLights[currRound][edge[0]] = not roundLights[currRound][edge[0]]
    # Redraw the updated graph
    drawGraph(roundPos[currRound], roundLights[currRound], roundEdges[currRound], roundSwitches[currRound])
    
# Check if the mouse position x, y is within one of the nodes' radius
def checkPos(x, y):
    for i in range(0, len(roundPos[currRound])):
        if sqrt((x-roundPos[currRound][i][0])**2 + (y-roundPos[currRound][i][1])**2) < circleRadius:
            return i
    return -1

# Reset round lights
def reset(round):
    roundLights[currRound] = [False]*len(roundPos[currRound])
    roundSwitches[currRound] = [False]*len(roundPos[currRound])
            
