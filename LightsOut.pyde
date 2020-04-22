onOutline = color(245, 197, 66);
onFill = color(245, 233, 66);
offOutline = color(0, 0, 0);
offFill = color(167, 167, 167);

round1Size = 2;
round1Pos = [[50,50], [150,150]];
round1Lights = [True, True];
round1Edges = [[0,1]];

def setup():
    size(500, 500)

def draw():
  drawGraph(round1Pos, round1Lights, round1Edges)


'''
Draw the graph with yellow circle at posArr[i] where lightOnArr[i] is True
'''
def drawGraph(posArr, lightOnArr, edgesArr):
  
  stroke(color(0,0,0))
  for edge in round1Edges:
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
        
      circle(posArr[i][0], posArr[i][1], 30)
