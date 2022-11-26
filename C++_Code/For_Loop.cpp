#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main() {
    // Complete the code.

    int a, b;
    cin>>a;
    cin>>b;
    map <int, string> Numbers;
    Numbers[1] = "one";
    Numbers[2] = "two";
    Numbers[3] = "three";
    Numbers[4] = "four";
    Numbers[5] = "five";
    Numbers[6] = "six";
    Numbers[7] = "seven";
    Numbers[8] = "eight";
    Numbers[9] = "nine";
    for (int i=a; i<=b; i++){
        if (i>=1 && i<=9){
            cout<<Numbers[i]<<endl;
        } else if(i>9){
            if (i%2==0){
                cout<<"even"<<endl;
            }else{
                cout<<"odd"<<endl;
            }
        }
    }
    return 0;
}
