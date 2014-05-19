#include <iostream>
#include <list>

using namespace std;

list <int> sum (const list <int> &a, const list <int> &b){
  int carry=0;
  list <int>::const_iterator iterA=a.begin ();
  list <int>::const_iterator iterB=b.begin ();
  list <int> c;
  while (iterA!=a.end () || iterB!=b.end () || carry>0){
    int dA=0, dB=0;
    if(iterA!=a.end ())
      dA=(*iterA);
    if(iterB!=b.end ())
      dB=(*iterB);
    carry += dA + dB;
    int nuevoDig = carry%10;
    c.push_back (nuevoDig);
    carry /=10;

    if(iterA!=a.end ())
      iterA++;
    if(iterB!=b.end ())
      iterB++;
  }
  return (c);
}

int main (){
  list <int> a;
  list <int> b;
  a.push_back (1);
  b.push_back (1);
  int numDigitos=1;
  int term;
  // Term=2 porque los 2 primeros términos ya los hemos calculado, al final del bucle, term===3
  for (term=2; numDigitos<1000; term++){
    if (term%2==0){
      a=sum (a, b);
      numDigitos = a.size ();
    }else{
      b=sum (a, b);
      numDigitos = b.size ();
    }
  }
  cout << term << endl;
}
