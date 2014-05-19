#include <iostream>
#include <cmath>

using namespace std;

int main (){
  // La suma de los números 1 a 100 (1+2+3+...+100) va a ser:((1+100)/2)*100
  int sum = (50*(1+100));
  long long int squareSum = sum*sum;

  // La suma de los cuadrados la vamos a hacer por fuerza bruta:
  long long int sumSquares=0;
  for (int i=1; i<=100; i++){
    sumSquares += i*i;
  }
  
  cout << squareSum-sumSquares << endl;
}
