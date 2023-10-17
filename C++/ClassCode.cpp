#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {
    //Declared variables and operation for std
    using namespace std; 
    vector<double> data;
    double num;

    //Input
    cout << "Enter numeric values (enter a non-numeric value to compile code, Non-numeric will be voided):\n";
    
    //While user inputs the numbers, num is stored
    while (cin >> num) {
        data.push_back(num);
    }
    
    // If data is not stored or empty, No numerical data was enter
    if (data.empty()) {
        cout << "No data entered. Exiting." << endl;
        return 1;
    }

    //The operation to calculate average , minimum, and maximum
    double sum = 0;
    double average = 0;
    double min = data[0];
    double max = data[0];

    for (const double& value : data) {
        sum += value;
        if (value < min) {
            min = value;
        }
        if (value > max) {
            max = value;
        }
    }
    //Output 
    average = sum / data.size();
    cout << "-------------------------" << endl;
    cout << "Data Analysis Results:\n";
    cout << "Total numbers entered: " << data.size() << endl;
    cout << "Sum: " << sum << endl;
    cout << "Average: " << average << endl;
    cout << "Minimum Number Inputted: " << min << endl;
    cout << "Maximum Number Inputted: " << max << endl;

    return 0;
}
