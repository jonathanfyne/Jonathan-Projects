#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    string filename;
    cin >> filename;

    ifstream inFile(filename);

    if (!inFile.is_open()) {
        cout << "Could not open file " << filename << endl;
        return 1;
    }

    string line;
    while (getline(inFile, line)) {
        
        size_t tab1 = line.find('\t');
        size_t tab2 = line.find('\t', tab1 + 1);
        size_t tab3 = line.find('\t', tab2 + 1);

        
        string category = line.substr(0, tab1);
        string name = line.substr(tab1 + 1, tab2 - tab1 - 1);
        string description = line.substr(tab2 + 1, tab3 - tab2 - 1);
        string availability = line.substr(tab3 + 1);

        
        if (availability == "Available") {
            cout << name << " (" << category << ") -- " << description << endl;
        }
    }

    inFile.close();
    return 0;
}
