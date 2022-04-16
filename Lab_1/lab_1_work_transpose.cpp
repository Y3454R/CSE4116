#include <bits/stdc++.h>

using namespace std;

int main() {
    int i, j, k, m, n;
    char ch;

    cout << "enter text: ";
    char txt[100];
    cin.getline(txt,100);

    cout << "m: ";
    cin >> m;
    cout << "n: ";
    cin >> n;
    char mt[m][n];
    k = 0;
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            if(txt[k] != '\0') {
                ch = txt[k];
                mt[i][j] = ch;
                k++;
            }
            else{
                mt[i][j] = ' ';
            }
        }
    }
    cout << "INPUT:\n";
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            cout << mt[i][j];
        }
        cout << endl;
    }
    cout << "\n\n";
    for(j = 0; j < n; j++) {
        for(i = 0; i < m; i++) {
            ch = tolower(mt[i][j]);
            cout << ch;
        }
        cout << endl;
    }
}
