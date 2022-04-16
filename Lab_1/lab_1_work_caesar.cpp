#include <bits/stdc++.h>

using namespace std;

int main() {
    int i, l, k;

    cout << "Plain text: ";
    char txt[100],ch;
    cin.getline(txt,100);
    cout << "Key: ";
    cin >> k;

    l = strlen(txt);

    for(i = 0; txt[i] != '\0'; i++) {

         ch = txt[i];
         if (ch >= 'a' && ch <= 'z'){
            ch = ch + k;
            if (ch > 'z') {
               ch = ch - ('z' - 'a' + 1);
            }
         }
         else if (ch >= 'A' && ch <= 'Z'){
            ch = ch + k;
            if (ch > 'Z'){
               ch = ch - ('Z' - 'A' + 1);
            }
         }
        ch = tolower(ch);
        txt[i] = ch;
    }
    printf("Encrypted text: %s\n", txt);
      for(int i = 0; txt[i] != '\0'; ++i) {
         ch = txt[i];

         if(ch >= 'a' && ch <= 'z') {
            ch = ch - k;
            if(ch < 'a'){
               ch = ch + 'z' - 'a' + 1;
            }
         }

         else if(ch >= 'A' && ch <= 'Z') {
            ch = ch - k;
            if(ch < 'A') {
               ch = ch + 'Z' - 'A' + 1;
            }
         }
         ch = toupper(ch);
         txt[i] = ch;
      }
      cout << "Decrypted message: " << txt;
}



