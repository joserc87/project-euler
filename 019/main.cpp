#include <iostream>

using namespace std;

bool bisiesto (int year){
  if (year%4==0 && (year%100!=0||year%4==0)){
    return (true);
  }else{
    return (false);
  }
}

int diasMes (int month, int year){
  switch (month){
  case 1:// JUNIO
  case 3:
  case 5:
  case 7:
  case 8:
  case 10:
  case 12:
    return (31);
    break;
  case 4:
  case 6:
  case 9:
  case 11:
    return (30);
    break;
  case 2:
    if (bisiesto (year))
      return (29);
    else
      return (28);
  }
}

int main (){
  int diaSemana=0; // Lunes
  int i=0;
  int day=0, month=0, year=1900;
  int longMonth=diasMes (month+1, year);
  while (year != 1901){
    day++;
    i++;
    diaSemana=(diaSemana+1)%7;
    if (day==longMonth){
      day=0;
      month++;
      if (month==12){
	month=0;
	year ++;
      }
      longMonth=diasMes (month+1, year);
    }
  }
  int cnt=0;
  while (year != 2001){
    if (diaSemana==6 && day==0){
      cnt++;
    }
    day++;
    i++;
    diaSemana=(diaSemana+1)%7;
    if (day==longMonth){
      day=0;
      month++;
      if (month==12){
	month=0;
	year ++;
      }
      longMonth=diasMes (month+1, year);
    }
  }
  cout << cnt << endl;
}
