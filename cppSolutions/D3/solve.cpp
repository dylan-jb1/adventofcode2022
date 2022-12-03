#include <fstream>
#include <String>
#include <iostream>
#include <set>
using namespace std;

int main() {
    ifstream myfile;
    myfile.open ("./input.txt");
    string line;
    int total = 0;
    int badgeTotal = 0;

    int lineNum = 0;
    int badgeList[52] = {0};
    while (myfile >> line) {
        int lineSize = line.size();

        set<char> set;
        std::set<char> badgeSet;

        bool found = false;

        for (int x = 0; x < lineSize; x++) {
            if (badgeSet.find(line[x]) == badgeSet.end()) {
                if ((line[x] - 'a') < 0) {
                    badgeList[(line[x] - 'A')+26]++;
                } else {
                    badgeList[(line[x] - 'a')]++;
                }
            }
            badgeSet.insert(line[x]);

            if (x >= lineSize/2) {
                if (!found && set.find(line[x]) != set.end()) {
                    // shared element
                    if ((line[x] - 'a') < 0) {
                        int score = (line[x] - 'A')+27;
                        total += score;
                    } else {
                        int score = (line[x] - 'a')+1;
                        total += score;
                    }
                    found = true;
                }
            } else {
                set.insert(line[x]);
            }
        }
        lineNum++;
        if (lineNum == 3) {
            lineNum = 0;
            for (int y = 0; y < 52; y++) {
                if (badgeList[y] == 3) {
                    badgeTotal+=y+1;
                }

                badgeList[y] = 0;
            }
        }
    }
    myfile.close();

    std::cout << total << endl; // part 1
    std::cout << badgeTotal << endl; // part 2

    return 0;
}