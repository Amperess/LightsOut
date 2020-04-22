color onOutline = color(245, 197, 66);
color onFill = color(245, 233, 66);
color offOutline = color(0, 0, 0);
color offFill = color(167, 167, 167);

int round1Size = 2;
int[][] round1Pos = { {50, 50}, {150, 150} };
boolean[] round1Lights = {true, true};
boolean[][] round1Edges = {{false, true}, {true, false}};



void setup() {
  size(500, 500);
}

void draw() {
  drawGraph(round1Pos, round1Lights, round1Edges);
}

/*
Draw the graph with yellow circle at posArr[i] where lightOnArr[i] is True
*/
void drawGraph(int[][] posArr, boolean[]lightOnArr, boolean[][]edgesArr){
  
  int startX = 0;
  int startY = 0;
  int endX = 0;
  int endY = 0;
  
  stroke(color(0,0,0));
  for(int r = 0; r < edgesArr.length; r++){
    for(int c = 0; c < edgesArr[0].length; c++){
      if(edgesArr[r][c] == true){
        startX = posArr[r][0];
        startY = posArr[r][1];
        endX = posArr[c][0];
        endY = posArr[c][1];
        line(startX, startY, endX, endY);
      }
    }
  }
  
  
  for(int i = 0; i < posArr.length; i++){
    if (lightOnArr[i] == true){
      stroke(onOutline);
      fill(onFill);
    } else {
      stroke(offOutline);
      fill(offFill);
    }
    circle(posArr[i][0], posArr[i][1], 30);
  }
  
}
