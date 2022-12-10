const fs = require('fs')
const readline = require('readline')

async function read() {
    const fileStream = fs.createReadStream("./input.txt");
    
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let first = 0;
    let second = 0;
    let third = 0;
    let total = 0;
    for await (const line of rl) {
        if (line.trim() == "") {
            if (total>first) {
                third=second;
                second=first;
                first=total;
            } else if (total > second) {
                third=second;
                second=total;
            } else if (total > third) {
                third=total;
            }
            total = 0;
        } else {
            total+=parseInt(line);
        }
    }   
    console.log(first); // part 1
    console.log(first+second+third); // part 2
}

read();