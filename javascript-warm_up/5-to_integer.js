#!/usr/bin/node

const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args)}`);
}
