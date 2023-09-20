#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

int GetWordFrequency(vector<string> wordsList, string currWord) {
    int count = 0;
    int numWords = wordsList.size(); // Get the number of words in the list

    for (int j = 0; j < numWords; j++) {
        
        // Convert the first character of each word to lowercase for comparison
        wordsList[j][0] = tolower(wordsList[j][0]);
        currWord[0] = tolower(currWord[0]);
        
        if (wordsList[j] == currWord) {
            count++;
        }
    }
    return count;
}

int main() {
    int numWords;
    vector<string> userWords;
    string currWord;

    // Read the number of words
    cin >> numWords;

    // Read user words and store them in a vector
    for (int i = 0; i < numWords; i++) {
        cin >> currWord;
        userWords.push_back(currWord);
    }

    // Count word frequencies and amount of time repeared and print results
    for (int i = 0; i < numWords; i++) {
        currWord = userWords[i];
        int wordFreq = GetWordFrequency(userWords, currWord);
        cout << currWord << " " << wordFreq << endl;
    }

    return 0;
}
