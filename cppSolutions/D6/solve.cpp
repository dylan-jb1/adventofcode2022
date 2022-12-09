#include <fstream>
#include <String>
#include <iostream>
#include <queue>
#include <chrono>
using namespace std;

typedef std::chrono::high_resolution_clock Clock;

int main() {
    ifstream myfile;
    myfile.open ("./input.txt");

    auto start_time = Clock::now();

    int p1=0,p2=0;

    string line;

    while (getline(myfile,line)) {
        int charArr[26] = {0};
        queue<int> last;
        int index = 0;
        int unique = 0;
        for (int x = 0; x < line.length(); x++) {
            if (charArr[line[x] - 'a'] > 0) {// if this letter was already present
            } else {
                unique++;
            }

            last.push((line[x] - 'a'));
            charArr[line[x] - 'a']++;

            if (last.size() > 4) {
                charArr[last.front()]--;
                if (charArr[last.front()] > 0)
                    unique--;
                last.pop();
            }

            if (unique == 4) {
                p1=x;
                cout << x << " " << unique << endl;
                break;
            }
        }
    }

    myfile.close();

    auto end_time = Clock::now();
    
    std::cout << "Time taken:" << chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count()/1000.0 << "ms" << std::endl;
    std::cout << "Total Part 1: " << p1 << endl; // part 1
    std::cout << "Total Part 2: " << p2 << endl; // part 2

    return 0;
}