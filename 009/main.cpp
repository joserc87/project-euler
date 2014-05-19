#include <iostream>

using namespace std;

int main (){
  int A, B, C;
  bool encontrado=false;
  for (int a=2; a<1000/3 && !encontrado; a++){
    for (int b=a+1; a+2*b<1000 && !encontrado; b++){
      int c = 1000-a-b;
      if (a*a+b*b==c*c){
	A=a;
	B=b;
	C=c;
	encontrado=true;
      }
    }
  }
  cout << A*B*C << endl;
}
