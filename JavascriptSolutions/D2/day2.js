const fs = require('fs')
const readline = require('readline')

async function read() {
    const fileStream = fs.createReadStream("./input.txt");
    
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const le = {
        A: 1,
        B: 2,
        C: 3,
        X:1,
        Y:2,
        Z:3
    }


    let score1 = 0;
    let score2 = 0;

    for await (const line of rl) {
        // CODE BELOW HERE

        const l = line.split(" ");
        const a= l[0], b = l[1];

        let play = le[a] + (le[b]-2);
        
        if (play == 0)
            play = 3;
        else if (play == 4)
            play = 1;

        score1 += le[b]
        score2 += play

        if (le[b] == 3)
            score2+=6;
        else if (le[b]==2)
            score2+=3;

        if ((((le[a])%3)+1) == le[b]) {
            // i win
            score1+=6
        } else if (le[a] == le[b]) {
            //draw
            score1+=3
        } else {
            // loss
        }
    }   
    console.log(score1); // part 1
    console.log(score2); // part 2
}

read();