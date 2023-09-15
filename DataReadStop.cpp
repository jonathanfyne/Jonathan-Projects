/*
Stops Reading Input when data stores non-positive integer. Program outputs the exception and positive integers only
Can be modified for larger data sets
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> inputIntegers;
    int value;

    // Read positive integers until a non-positive integer is encountered
    while (true) {
        cin >> value;

        if (value <= 0) {
            break; // Exit the loop when a non-positive integer is encountered
        }

        inputIntegers.push_back(value); // Add positive integer to the vector
    }

    // Print the positive integers
    for (int i = 0; i < inputIntegers.size(); ++i) {
        cout << inputIntegers.at(i) << endl;
    }

    return 0;
}
