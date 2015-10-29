#include <utility>
#include <vector>
#include <string>

#include <fstream>
#include <iostream>
#include <sstream>

#include <math.h>

#define INPUT_PATH "/home/raca/tmp/p099_base_exp.txt"

using namespace std;

typedef pair<unsigned int, unsigned int> tPairInt;
typedef vector<tPairInt> tVecPairs;

void loadPairs(string _fileName, tVecPairs& numbers);
int findMax(tVecPairs _pairs);
bool operator>(tPairInt& a, tPairInt& b);

int main(int argc, char* argv[]){
    tVecPairs pairs;
    loadPairs(INPUT_PATH, pairs);
    cout << "Biggest number is in line: " << findMax(pairs) << endl;
    return 0;
}

void loadPairs(string _fileName, tVecPairs& numbers){
    char buffer[255];
    ifstream inStream(_fileName);
    string base, expo;
    numbers.clear();
    numbers.reserve(1000);
    while(!inStream.eof()){
        inStream.getline(buffer, 256);
        istringstream tmpStream(buffer);
        getline(tmpStream, base, ',');
        getline(tmpStream, expo, ',');
        numbers.push_back(tPairInt(atoi(base.c_str()), atoi(expo.c_str())));
    }
}

int findMax(tVecPairs _pairs){
    int maxIdx = 1;
    tPairInt maxPair = _pairs[0];
    for(int i=1; i < _pairs.size(); i++){
        if( _pairs[i] > maxPair ){
            maxPair = _pairs[i];
            maxIdx = i+1;
        }
    }
    return maxIdx;
}

bool operator>(tPairInt& a, tPairInt& b){
    return a.second*log(a.first) > b.second*log(b.first);
}

//      My very stupid solution before reading... I mean remembering.. to use the log

//bool operator>(tPairInt& a, tPairInt& b){
////    cout << "Comparing: " << a.first << " to " << b.first << endl;
//    bool baseBigger = false, expoBigger = false;
//    if(a.first > b.first)
//        baseBigger = true;
//    if(a.second > b.second)
//        expoBigger = true;
//    if(baseBigger && expoBigger)
//        return true;
//    if(!baseBigger && !expoBigger)
//        return false;
//    // t & f || f & t
//    double a_base = a.first,
//           b_base = b.first,
//           a_expo = a.second,
//           b_expo = b.second;
//    if(baseBigger){ // A bigger base, B bigger expo
//        double baseRate = a_base/b_base,
//               expoDiff = b_expo - a_expo;
//        if( pow(baseRate, a_expo) > pow(b_base, expoDiff) )
//            return true;
//        return false;
//    }
//    // A bigger expo, B bigger base
//    double baseRate1 = b_base/a_base,
//           expoDiff1 = a_expo - b_expo;
//    if( pow(baseRate1, b_expo) > pow(a_base, expoDiff1) )
//        return false;
//    return true;
//}

