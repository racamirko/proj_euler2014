#include <list>
#include <stdio.h>

void generatePrimes(int _maxNum, std::list<int>& _foundPrimes);

int main(){
	return 0;
}

void generatePrimes(int _maxNum, std::list<int>& _foundPrimes){
  bool* isOrIsnt = new bool[_maxNum];
  memset(isOrIsnt, true, _maxNum);


  for(unsigned i = 2; i < _maxNum; ++i){

  }

  delete [] isOrIsnt;
}