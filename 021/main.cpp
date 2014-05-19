#include <iostream>
#include <cmath>
#include <list>
#include <set>

using namespace std;

bool calcularPrimos (list <long int> &primos, int hasta){
  bool cambia=false;
  int i;
  if (primos.size () == 0){
    primos.push_back (2);
    cambia=true;
    i=3;
  }else{
    i=primos.back ()+2;
  }

  while (i<hasta){
    bool esPrimo=true;
    int raiz = (int)sqrt(i);
    for (list <long int>::const_iterator iter = primos.begin (); iter != primos.end () && (*iter)<=raiz; iter++){
      if (i%(*iter)==0)
	esPrimo=false;
    }
    if (esPrimo){
      primos.push_back (i);
      cambia=true;
    }
    i+=2;
  }
  return (cambia);
}

list <long int> divisoresPrimos (long int n, list <long int> &primos){
  //  calcularPrimos (primos, n);

  list <long int> divisores;
  bool cambia=true;
  while (cambia && n!=1){
    for (list <long int>::const_iterator iter = primos.begin (); iter != primos.end () && n != 1; iter++){
      while (n%(*iter)==0){
	divisores.push_back ((*iter));
	n/=(*iter);
      }
    }
    cambia=calcularPrimos (primos, n);
  }
  return (divisores);
}

set <long int> divisores (long int n, list <long int> &primos){
  list <long int> divPrim = divisoresPrimos (n, primos);
  set <long int> divs;
  divs.insert (1);
  for(list <long int>::const_iterator iter = divPrim.begin (); iter != divPrim.end (); iter++){
    set <long int> divsCpy = divs;
    for (set <long int>::const_iterator iter2 = divsCpy.begin (); iter2 != divsCpy.end (); iter2++){
      long int mul = (*iter)*(*iter2);
      if (mul<n)
	divs.insert (mul);
    }
  }
  return (divs);
}

int sumDivisores (long int n, list <long int> &primos){
  set <long int> divs = divisores (n, primos);
  int cnt=0;
  for (set<long int>::iterator iter = divs.begin (); iter != divs.end (); iter++){
    cnt += (*iter);
  }
  return (cnt);
}

int main (){
  long int i=1;
  long int t;
  int div;

  // Calcular unos cuantos primos
  list <long int> primos;
  calcularPrimos (primos, 100000);
  long int sum=0;
  set <long int> amigos;
  for (int i=2; i<=10000; i++){
    if (amigos.count (i)<=0){
      int amigo = sumDivisores (i, primos);
      if (amigo<10000 && i!=amigo && i==sumDivisores (amigo, primos)){
	amigos.insert (i);
	amigos.insert (amigo);
      }
    }
  }
  for (set <long int>::const_iterator iter = amigos.begin (); iter != amigos.end (); iter++){
    sum+=(*iter);
  }
  cout << sum << endl;
}
