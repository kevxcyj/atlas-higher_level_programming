#!/usr/bin/node
// Script that writes a string to a file
const fs = require('fs');

if (process.argv.length === 3) {
  console.error('An error has occured');
  process.exit(1);
}

const filePath = process.argv[2];
const userString = process.argv[3];

fs.writeFile(filePath, userString, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
