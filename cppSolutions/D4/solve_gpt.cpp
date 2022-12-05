#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

struct Range {
    int start, end;
};

// Compare two ranges for sorting
bool compare(const Range& a, const Range& b) {
    if (a.start == b.start) return a.end < b.end;
    return a.start < b.start;
}

// Check if range a contains range b
bool contains(const Range& a, const Range& b) {
    return a.start <= b.start && a.end >= b.end;
}

// Check if range a overlaps with range b
bool overlaps(const Range& a, const Range& b) {
    return !(a.end < b.start || b.end < a.start);
}

int main() {
    vector<Range> ranges;
    string line;
    ifstream myfile;
    myfile.open("./input.txt");

    while (getline(myfile, line)) {
        int start = stoi(line.substr(0, line.find('-')));
        int end = stoi(line.substr(line.find('-') + 1));
        ranges.push_back({start, end});
    }

    sort(ranges.begin(), ranges.end(), compare);

    int num_fully_contained = 0;
    int num_overlap = 0;
    for (int i = 0; i < ranges.size(); i++) {
        for (int j = i + 1; j < ranges.size(); j++) {
            if (contains(ranges[i], ranges[j])) {
                num_fully_contained++;
            } else if (overlaps(ranges[i], ranges[j])) {
                num_overlap++;
            }
        }
    }

    cout << "Number of fully contained pairs: " << num_fully_contained << endl;
    cout << "Number of overlapping pairs: " << num_overlap << endl;

    return 0;
}
