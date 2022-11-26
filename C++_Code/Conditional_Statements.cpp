#include <bits/stdc++.h>
#include <map>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    map<int, string> Numbers;
    Numbers[1]="one";
    Numbers[2] = "two";
    Numbers[3]="three";
    Numbers[4] = "four";
    Numbers[5]="five";
    Numbers[6] = "six";
    Numbers[7]="seven";
    Numbers[8] = "eight";
    Numbers[9]="nine";


    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    // Write your code here
    if (n>=1 && n<=9){
        cout<<Numbers[n];
    }
    else if (n>9){
        cout<<"Greater than 9";
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
