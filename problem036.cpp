#include <iostream>
#include <string>
#include <bitset>

using namespace std;

bool checkPalindromeText(string _text);
bool checkPalindromeBin(unsigned _num);
bool checkPalindromeDec(unsigned _num);
string trimZeros(string _binNum);

int main(){
    unsigned summ = 0;
    for(unsigned i = 1; i < 1000000; i++)
        if(checkPalindromeDec(i) && checkPalindromeBin(i)){
            summ += i;
        }
    cout << "Sum = " << summ << endl;
}

bool checkPalindromeDec(unsigned _num){
    return checkPalindromeText(to_string(_num));
}

bool checkPalindromeBin(unsigned _num){
    string text = bitset<21>(_num).to_string();
    return checkPalindromeText(trimZeros(text));
}

string trimZeros(string _binNum){
    for(unsigned i = 0; i < _binNum.length(); i++){
        if(_binNum[i] != '0')
            return _binNum.substr(i, _binNum.length()-i);
    }
    return _binNum;
}

bool checkPalindromeText(string _text){
    int textLen = _text.length();
    for(short i = 0; i < textLen/2+1; ++i){
        short pos2 = textLen-i-1;
        if(_text[pos2] != _text[i])
            return false;
    }
    return true;
}
