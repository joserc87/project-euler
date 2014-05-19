#include <iostream>
#include <vector>

using namespace std;

long int caminos (int x, int y, int xfin, int yfin, vector <vector <long int> > &ncam){
  long int numCaminos=0;
  if (ncam [x][y]>0){
    return (ncam [x][y]);
  }
  if (x<xfin){
    numCaminos += caminos (x+1, y, xfin, yfin, ncam);
  }
  if (y<yfin){
    numCaminos += caminos (x, y+1, xfin, yfin, ncam);
  }
  if (x==xfin && y==yfin){
    numCaminos=1;
  }
  ncam [x][y]=numCaminos;
  return (numCaminos);
}

int main (){
  vector <vector <long int> > ncam (21, vector <long int> (21, -1));
  long int numCaminos = caminos (0,0,20,20, ncam);
  cout << numCaminos << endl;
}
