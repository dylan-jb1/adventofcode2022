#include <fstream>
#include <String>
#include <iostream>
#include <stack>
#include <chrono>
#include <vector>
#include <algorithm>
using namespace std;

typedef std::chrono::high_resolution_clock Clock;

int main() {
    ifstream myfile;
    myfile.open ("./input_6mb.txt");

    auto start_time = Clock::now();

    string line = "";
    bool initStack = true;

    vector<stack<char>> stacks;
    vector<stack<char>> stacksP2;
    vector<string> lines;

    while (getline(myfile,line)) {
        if (initStack) { // find stacks
            if (line.find('1') != string::npos) { // if this line defines the number of stacks
                initStack = false;
                reverse(lines.begin(), lines.end());
                for (string initLine : lines) {
                    string tempLine = initLine;
                    tempLine.append(line.length() - initLine.length(),' ');
                    int stackCount = 0;
                    for (int x = 0; x < line.length(); x++) {
                        if (isalpha(tempLine[x]) != 0) { // if it's a letter
                            if (stacks.size() < atoi(line.substr(x,1).c_str())) { // if stack doesnt exist
                                stack<char> newStack;
                                newStack.push(tempLine[x]);
                                stacks.push_back(newStack);
                            } else {
                                stacks[atoi(line.substr(x,1).c_str())-1].push(tempLine[x]);
                            }
                        }
                    }
                }
                stacksP2 = stacks;
            } else {
                lines.push_back(line);
            }
        } else {
            int firstSpace = line.find(" ");
            int secondSpace = line.find(" ",firstSpace+1);
            int thirdSpace = line.find(" ",secondSpace+1);
            int fourthSpace = line.find(" ",thirdSpace+1);
            int fifthSpace = line.find(" ",fourthSpace+1);

            if (!(firstSpace == -1 || secondSpace == -1 || thirdSpace == -1 || fourthSpace == -1 || fifthSpace == -1)) {
                int count = stoi(line.substr(firstSpace+1,secondSpace).c_str());
                int from = stoi(line.substr(thirdSpace+1,fourthSpace).c_str());
                int to = stoi(line.substr(fifthSpace+1).c_str());

                for (int x = 0; x < count; x++) {
                    stacks[to-1].push(stacks[from-1].top());
                    stacks[from-1].pop();
                }

                string newOrd = "";
                for (int x = 0; x < count; x++) {
                    newOrd.push_back(stacksP2[from-1].top());
                    stacksP2[from-1].pop();
                }
                for (int x = newOrd.length()-1; x >= 0 ; x--) {
                    stacksP2[to-1].push(newOrd[x]);
                }
            }
        }
    }

    string p1;
    string p2;
    for (auto stack : stacks) {
        p1.push_back( stack.top());
    }

    for (auto stack : stacksP2) {
        p2.push_back( stack.top());
    }

    myfile.close();

    auto end_time = Clock::now();
    
    std::cout << "Time taken:" << chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count()/1000.0 << "ms" << std::endl;
    std::cout << "Total Part 1: " << p1 << endl; // part 1
    std::cout << "Total Part 2: " << p2 << endl; // part 2

    return 0;
}