#include <fstream>
#include <String>
#include <iostream>
#include <set>
#include <chrono>
using namespace std;

typedef std::chrono::high_resolution_clock Clock;

int main() {
    ifstream myfile;
    myfile.open ("./input.txt");

    auto start_time = Clock::now();

    int p1=0,p2=0;

    string line;

    while (myfile >> line) {
        int e1s1=0,e1s2=0,e2s1=0,e2s2=0;
        int count = 0;
        string lineNum = "";
        for (int x = 0; x < line.size(); x++) { // set ranges
            if (line[x]=='-'||line[x]==','||line[x]=='\0') {
                if (count==0) {
                    e1s1=stoi(lineNum);
                } else if (count==1) {
                    e1s2=stoi(lineNum);
                } else if (count == 2) {
                    e2s1=stoi(lineNum);
                } else {
                    e2s2=stoi(lineNum);
                }
                lineNum = "";
                count++;
            } else {
                lineNum.push_back(line[x]);
            }
        }
        e2s2=stoi(lineNum);

        bool found = false;

        if (e1s1 <= e2s1) {
            if (e1s2 >= e2s2) {
                p1++;
                found=true;
            }
        }
        if (e2s1 <= e1s1) {
            if (!found && e2s2 >= e1s2) {
                p1++;
            }
        }

        if ((e1s1 <= e2s1 && e1s2 >= e2s1)||(e1s1 <= e2s2 && e1s2 >= e2s2)||(e2s1 <= e1s1 && e2s2 >= e1s1)||(e2s1 <= e1s2 && e2s2 >= e1s2))
            p2++;
    }

    myfile.close();

    auto end_time = Clock::now();
    
    std::cout << "Time taken:" << chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count()/1000.0 << "ms" << std::endl;
    std::cout << "Total Part 1: " << p1 << endl; // part 1
    std::cout << "Total Part 2: " << p2 << endl; // part 2

    return 0;
}