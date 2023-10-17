#include <iostream>
#include <string>
using namespace std;

int main() {
   
   string userInput, userInputNoSpaces;

   
   getline(cin, userInput); // The same as cin >> userInput
   
   for(int i=0; i < userInput.size(); i++){ // loop continues if condition - (i < userinputsize) - is correct
   // i starts from 0 , increases by 1. i only accessible to this for loop since defined in for loop
      
   if (isalpha(userInput.at(i))){
      userInputNoSpaces += userInput.at(i);
   }
   }
   cout << userInputNoSpaces << endl;
   return 0;
   
}