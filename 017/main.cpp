#include <iostream>

using namespace std;

int numLetras (int num){
  int unidades []={
    0, // Nada
    3, // ONE
    3, // TWO
    5, // THREE
    4, // FOUR
    4, // FIVE
    3, // SIX
    5, // SEVEN
    5, // EIGHT
    4, // NINE
    3, // TEN
    6, // ELEVEN
    6, // TWELVE
    8, // THIRTEEN
    8, // FOURTEEN
    7, // FIFTEEN
    7, // SIXTEEN
    9, // SEVENTEEN
    8,  // EIGHTEEN
    8 // NINETEEN
  };

  int decenas []={
    0, // Nada
    4, // TEEN
    6, // TWENTY
    6, // THIRTY
    5, // FORTY
    5, // FIFTY
    5, // SIXTY
    7, // SEVENTY
    6, // EIGHTY
    6  // NINETY
  };

  if (num==1000){
    return (11); // ONE THOUSAND
  }

  int numLetras=0;
  int cent=num/100;
  int dec= (num/10)%10;
  int uni=num%10;
  if (dec == 1){
    dec = 0;
    uni += 10;
  }

  numLetras += unidades [uni];
  numLetras += decenas [dec];
  if (cent>0){
    numLetras += unidades [cent]; // TWO
    numLetras += 7; // HUNDRED
    if (dec!=0 || uni!=0)
      numLetras += 3; // AND
  }
  return (numLetras);
}

void escribir (int num){
  char unidades [][10]={
    "",// Nada
    "ONE", // ONE
    "TWO", // TWO
    "THREE", // THREE
    "FOUR", // FOUR
    "FIVE", // FIVE
    "SIX", // SIX
    "SEVEN", // SEVEN
    "EIGHT", // EIGHT
    "NINE", // NINE
    "TEN", // TEN
    "ELEVEN", // ELEVEN
    "TWELVE", // TWELVE
    "THIRTEEN", // THIRTEEN
    "FOURTEEN", // FOURTEEN
    "FIFTEEN", // FIFTEEN
    "SIXTEEN", // SIXTEEN
    "SEVENTEEN", // SEVENTEEN
    "EIGHTEEN", // EIGHTEEN
  };

  char decenas [][10]={
    "", // Nada
    "TEEN", // TEEN
    "TWENTY", // TWENTY
    "THIRTY", // THIRTY
    "FORTY", // FORTY
    "FIFTY", // FIFTY
    "SIXTY", // SIXTY
    "SEVENTY", // SEVENTY
    "EIGHTY", // EIGHTY
    "NINETY"  // NINETY
  };

  if (num==1000){
    cout << "ONE THOUSAND";
    return;
  }

  int cent=num/100;
  int dec= (num/10)%10;
  int uni=num%10;
  if (dec == 1){
    if (uni <= 8){
      dec = 0;
      uni += 10;
    }
  }

  if (cent>0){
    cout << unidades [cent] << " HUNDRED ";
    if (dec!=0 || uni!=0)
      cout << "AND ";
  }
  if (dec>1){
    cout << decenas [dec];
    if (uni>0)cout << "-";
  }
  cout << unidades [uni];
  if (dec==1){
    cout << decenas [dec];
  }

}


int main (){
  int acc=0;
  for (int i=1; i<=1000; i++){
    acc += numLetras (i);
  }
  cout << acc << endl;
}
