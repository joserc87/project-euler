#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <list>

using namespace std;

string readName (ifstream &fi){
  char name [256];
  char c=' ';
  bool primeraComilla=false;
  fi.get (name, 256, ',');
  c=fi.get ();
  int l=strlen (name);
  name[l-1]='\0';
  string s = name+1;

  return (s);
}

int worth (string s){
  int cnt=0;
  for (int i=0; i<s.length (); i++){
    cnt += s [i]-'A'+1;
  }
  return (cnt);
}

int main (){
  ifstream fi;
  fi.open ("./names.txt");
  if (!fi){
    cerr << "ERROR: El archivo names.txt no se puede abrir" << endl;
    return (-1);
  }
  list <string> nombres;
  while (fi.good ()){
    string name = readName (fi);
    if (name.size ()>0){
      nombres.push_back (name);
    }
  }
  fi.close ();

  nombres.sort ();
  long int scoreAccum=0;
  int i=1;
  for (list <string>::const_iterator iter = nombres.begin (); iter != nombres.end (); iter++, i++){
    int score = worth (*iter)*i;
    scoreAccum += score;
  }

  cout << scoreAccum << endl;
}
