#include <iostream>
#include <fstream>

using namespace std;

int main (){
  ifstream fi;
  fi.open ("grid.txt");
  if (!fi){
    cerr << "No se puede abrir el archivo grid.txt" << endl;
    return (-1);
  }
  int grid [20][20];
  for (int i=0; i<20; i++){
    for (int j=0; j<20; j++){
      fi >> grid [i][j];
    }
  }
  fi.close ();
  long int maxMult=0;
  // Recorremos todas las casillas
  for (int i=0; i<20; i++){
    for (int j=0; j<20; j++){
      // Derecha
      if (j<20-3){
	long int mult = 1;
	for (int s=0; s<4; s++){
	  mult = mult * grid [i][j+s];
	}
	if (mult>maxMult)
	  maxMult=mult;
      }
      // Abajo
      if (i<20-3){
	long int mult = 1;
	for (int s=0; s<4; s++){
	  mult = mult * grid [i+s][j];
	}
	if (mult>maxMult)
	  maxMult=mult;
      }
      // Diagonal 1
      if (i<20-3 && j<20-3){
	long int mult = 1;
	for (int s=0; s<4; s++){
	  mult = mult * grid [i+s][j+s];
	}
	if (mult>maxMult){
	  maxMult=mult;
	}
      }
      // Diagonal 2
      if (i<20-3 && j>=3){
	long int mult = 1;
	for (int s=0; s<4; s++){
	  mult = mult * grid [i+s][j-s];
	}
	if (mult>maxMult)
	  maxMult=mult;
      }
    }
  }

  cout << maxMult << endl;
}
