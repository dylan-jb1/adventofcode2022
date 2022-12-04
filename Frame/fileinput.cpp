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
        
    }

    myfile.close();

    auto end_time = Clock::now();
    
    std::cout << "Time taken:" << chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count() << "ns" << std::endl;
    std::cout << "Total Part 1: " << p1 << endl; // part 1
    std::cout << "Total Part 2: " << p2 << endl; // part 2

    return 0;
}