#include <iostream>
#include <list>

using namespace std;

void pow2 (list <int> &num){
  int carry=0;
  for (list <int>::iterator iter = num.begin (); iter != num.end (); iter++){
    int n=(*iter)*2+carry;
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
  for (int i=0; i<1000; i++){
    pow2 (num);
  }
  int sum=0;
  for (list <int>::const_iterator iter = num.begin (); iter != num.end (); iter++){
    sum += (*iter);
  }
  cout << sum << endl;

}
