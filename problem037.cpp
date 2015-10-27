#include <iostream>
#include <stdio.h>
#include <memory.h>

using namespace std;

void generatePrimes(int _arrayLimit, unsigned int** _out, unsigned int* _primesFound);
void testPrimeGenerator();
void testCheckPrimes();
bool isPrime(unsigned int _num, unsigned int* _primeSet, unsigned int _primeLength);
bool checkLeftRight(unsigned int _num, unsigned int* _primeSet, unsigned int _primeLength);

int main(){
//    testPrimeGenerator();
//    testCheckPrimes();
    unsigned int* myPtr = NULL;
    unsigned int primeCnt = 0;
    generatePrimes(1000000, &myPtr, &primeCnt);
    // print primes
    unsigned int primeSum = 0;
    for(int i(0); i < primeCnt; i++){
        if(myPtr[i] < 10)
            continue;
        if( checkLeftRight(myPtr[i], myPtr, primeCnt) ){
            printf("Found %d\n", myPtr[i]);
            primeSum += myPtr[i];
        }
    }
    printf("Sum: %d\n", primeSum);
    delete [] myPtr;
    return 0;
}

bool checkLeftRight(unsigned int _num, unsigned int* _primeSet, unsigned int _primeLength){
    unsigned int curNum = _num;
    // remove from left side
    while(curNum>0){
        if(!isPrime(curNum, _primeSet, _primeLength))
            return false;
        curNum /= 10;
    }
    curNum = _num;
    // find number of decimals
    unsigned int decs = 10;
    while(_num > decs)
        decs*=10;
    decs /= 10;
    while(curNum>0){
        if(!isPrime(curNum, _primeSet, _primeLength))
            return false;
        curNum %= decs;
        decs /= 10;
    }
    return true;
}

void testPrimeGenerator(){
    unsigned int* myPtr = NULL;
    unsigned int primeCnt = 0;
    generatePrimes(1000000, &myPtr, &primeCnt);
    // print primes
    for(int i(0); i < primeCnt; i++){
        printf("%d, ", myPtr[i]);
    }
}

void testCheckPrimes(){
    unsigned int* myPtr = NULL;
    unsigned int primeCnt = 0;
    generatePrimes(1000000, &myPtr, &primeCnt);
    if(isPrime(11, myPtr, primeCnt))
        printf("11 is correct\n");
    if(isPrime(998071, myPtr, primeCnt))
        printf("998071 is correct\n");
    if(!isPrime(500, myPtr, primeCnt))
        printf("500 is correct\n");
    if(!isPrime(1000001, myPtr, primeCnt))
        printf("1000001 is correct\n");
}

void generatePrimes(int _arrayLimit, unsigned int** _out, unsigned int* _primesFound){
    bool* allBools = new bool[_arrayLimit];
    memset(allBools, false, _arrayLimit*sizeof(bool));
    allBools[0] = true; allBools[1] = true;
    for(int i(2); i < _arrayLimit/2; i++)
        for(int j(2); j < _arrayLimit; j++){
            if(i*j >= _arrayLimit)
                break;
            allBools[i*j] = true;
        }
    // find the ones which remain
    unsigned int tmpVec[100000],
                 tmpVecLength = 0;
    for(int i(0); i < _arrayLimit; i++)
        if(!allBools[i])
            tmpVec[tmpVecLength++] = i;
    // prepare the final output
    *_primesFound = tmpVecLength;
    *_out = new unsigned int[tmpVecLength];
    memcpy(*_out, tmpVec, tmpVecLength*sizeof(unsigned int));
    // cleanup
    delete [] allBools;
}

bool isPrime(unsigned int _num, unsigned int* _primeSet, unsigned int _primeLength){
    // range checks
    if(_num < 2 || _num > _primeSet[_primeLength-1])
        return false;
    // halving
    unsigned int index = _primeLength/2,
                 stepSize = _primeLength/4;
    while(!(_primeSet[index] == _num || ( _primeSet[index-1]<_num && _primeSet[index]>_num )) ){
      if(_primeSet[index] > _num)
            index -= stepSize;
        else
            index += stepSize;
        if(stepSize > 1)
            stepSize /= 2;
    }
    return _primeSet[index] == _num;
}

