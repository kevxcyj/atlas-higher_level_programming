#!/usr/bin/node
// Script that reads and prints contents of file

const fs = require('fs');

if (process.argv.length === 2) {
  console.error('An error has occured');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(data);
});
