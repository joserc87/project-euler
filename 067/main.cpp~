#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main (){
  vector <vector <int> >triangle (15);
  vector <vector <int> >suma (15);
  for (int i=0; i<15; i++){
    triangle [i] = vector <int> (i+1);
    suma [i] = vector <int> (i+1);
  }
  ifstream fi;
  fi.open ("triangle.txt");
  if (!fi){
    cerr << "ERROR: El archivo triangle.txt no se puede abrir " << endl;
    return (-1);
  }

  for (int i=0; i<15; i++){
    for (int j=0; j<=i; j++){
      fi >> triangle [i][j];
    }
  }
  fi.close ();

  for (int i=0; i<15; i++){
    suma [14][i]=triangle[14][i];
  }

  for (int i=13; i>=0; i--){
    for (int j=0; j<=i; j++){
      int a = suma [i+1][j];
      int b = suma [i+1][j+1];
      int max = (a>b?a:b);
      suma [i][j] = triangle [i][j]+max;
    }
  }
  cout << suma [0][0] << endl;
}
