#include <iostream>
#include <list>

using namespace std;

void mult (list <int> &num, int x){
  int carry=0;
  for (list <int>::iterator iter = num.begin (); iter != num.end (); iter++){
    int n=(*iter)*x+carry;
    (*iter) = n%10;
    carry = n/10;
  }
  while (carry>0){
    num.push_back (carry%10);
    carry /= 10;
  }
}

int main(){
  list <int> num;num.push_back (1);
  for (int i=2; i<=100; i++){
    mult (num, i);
  }
  long int sum=0;
  for (list <int>::const_iterator iter = num.begin (); iter != num.end (); iter++){
    sum += (*iter);
  }
  cout << sum << endl;

}
