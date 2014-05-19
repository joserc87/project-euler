/**
 * Problem 34
 */

#include <iostream>
#include <vector>

using namespace std;



int main (){
	int fact [10];
	fact [0] = fact [1] = 1;
	for (int i=2; i<10; i++){
		fact [i] = i * fact [i-1];
	}
	
	long sum = 0;
	int i=3;
	bool bound = false;
	while (!bound){
		int sumFact = 0;
		int iCpy = i;
		bool all9s = true;

		while (iCpy>0){
			int digit = iCpy%10;
			sumFact += fact [digit];
			iCpy /= 10;
			if (digit != 9){
				all9s = false;
			}
		}
		if (sumFact == i){
			sum += i;
		}

		if (all9s && sumFact < i){
			bound = true;
		}
		i++;
	}
	cout << "Solution: " << sum << endl;
}
