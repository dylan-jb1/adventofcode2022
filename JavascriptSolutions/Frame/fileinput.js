const fs = require('fs')
const readline = require('readline')

async function read() {
    const fileStream = fs.createReadStream("./input.txt");
    
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        // CODE BELOW HERE

        
    }   
}

read();