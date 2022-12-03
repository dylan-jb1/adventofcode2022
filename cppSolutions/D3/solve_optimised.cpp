#include <iostream>
#include <fstream>
#include <string>
#include <chrono>

typedef std::chrono::high_resolution_clock Clock;

int main () {
    std::ifstream myfile;
    myfile.open ("./input.txt");

    auto start_time = Clock::now();

    std::string line;
    int total = 0;
    int badgeTotal = 0;

    int lineIter = 0;

    uint64_t e1 = uint64_t(0);
    uint64_t e2 = uint64_t(0);
    uint64_t e3 = uint64_t(0);

    while (myfile >> line) {
        uint64_t letters = uint64_t(0);
        int lineSize = line.size();

        bool found = false;

        for (int x = 0; x < lineSize; x++) {
            int letterVal;

            if (line[x] < 'a') {
                // capital
                letterVal = (line[x] - 'A')+27;
            } else {
                letterVal = (line[x] - 'a')+1;
            }

            uint64_t *e;

            if (lineIter==0)
                e=&e1;
            else if (lineIter==1)
                e=&e2;
            else
                e=&e3;

            *e |= (uint64_t(1) << letterVal);

            if (!found) {
            if (x < lineSize/2) {
                letters |= (uint64_t(1) << letterVal);
            } else {
                if ((letters & (uint64_t(1) << letterVal)) != 0) {
                    // shared letter
                    total += letterVal;
                    found = true; // dont check rest of letters
                }
            }
            }
        }

        lineIter++;
        if (lineIter == 3) {
            lineIter = 0;
            uint64_t eAll = e1&e2&e3;
            for (int z = 0; z < 64; z++) {
                if ((eAll & (uint64_t(1)<<z)) != 0) {
                    badgeTotal+=z;
                    break;
                }
            }
            e1 = 0, e2 = 0, e3 = 0;
        }
    }

    auto end_time = Clock::now();
    
    std::cout << "Total Part 1: " << total << std::endl;
    std::cout << "Total Part 2: " << badgeTotal << std::endl;
    std::cout << "Time taken:" << std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count() << "ns" << std::endl;

    myfile.close();
}