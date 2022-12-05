#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
  // Open the input file
  std::ifstream input("./input.txt");

  // Read all lines from the input file
  std::vector<std::string> lines;
  std::string line;
  while (std::getline(input, line)) {
    lines.push_back(line);
  }

  // Part 1
  int count = 0;
  for (const auto &line : lines) {
    // Split the line in two equal-sized strings
    std::string string1 = line.substr(0, line.size() / 2);
    std::string string2 = line.substr(line.size() / 2);

    for (char c : string1) {
      if (string2.find(c) != std::string::npos) {
        // The character appears in both strings, so add its value to the count
        if (isalpha(c)) {
          count += islower(c) ? (c - 'a' + 1) : (c - 'A' + 1);
        }
        break;
      }
    }
  }
  std::cout << count << std::endl;

  // Part 2
  count = 0;
  for (int i = 0; i < lines.size(); i += 3) {
    for (char c : lines[i]) {
      // Check if the character appears in the following two lines
      if (lines[i + 1].find(c) != std::string::npos && lines[i + 2].find(c) != std::string::npos) {
        // The character appears in all three lines, so add its value to the count
        if (isalpha(c)) {
          count += islower(c) ? (c - 'a' + 1) : (c - 'A' + 1);
        }
        break;
      }
    }
  }
  std::cout << count << std::endl;

  return 0;
}