#!/usr/bin/node
// Script that reads and prints contents of file

const fs = require('fs')

if (process.argv.length < 3) {
    console.log('Usage: node script.js <file_path>');
    process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('An error occurred: ${err}');
        return;
    }
    console.log(data);
});
