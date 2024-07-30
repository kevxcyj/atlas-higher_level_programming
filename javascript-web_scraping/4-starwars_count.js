#!/usr/bin/node
// Script that prints the number of movies where
// the character "Wedge Antilles" is present

const request = require('request');

if (process.argv.length === 2) {
  console.error('An error has occured');
  process.exit(1);
}

// The URL for SW AOI & ID for character
const url = process.argv[2];
const characterID = '18';

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let appearenceCount = 0;

    // Check through each file for results
    for (const film of films.results) {
      for (const char of film.characters) {
        if (char.endsWith(`/${characterID}/`)) {
          appearenceCount++;
        }
      }
    }
    console.log(appearenceCount);
  }
});
