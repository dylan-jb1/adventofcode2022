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

        const lineSize = line.length;

        const str1 = line.substring(0,lineSize/2);
        const str2 = line.substring(lineSize/2);

        for (let x = 0; x < str1.length; x++) {
            if (str2.includes(str1[x])) {
                
            }
        }
    }   
}

read();