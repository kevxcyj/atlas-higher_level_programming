#!/usr/bin/node
// Script that prints the title of a Star Wars movie where
// the episode number matches a given integer

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

request.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (e) {
      console.log('Error:', e);
    }
  }
});
