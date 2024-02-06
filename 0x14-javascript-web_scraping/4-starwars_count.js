#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    const count = results.reduce((total, movie) => {
      const hasCharacter18 = movie.characters.some((character) => character.endsWith('/18/'));
      return hasCharacter18 ? total + 1 : total;
    }, 0);
    console.log(count);
  }
});
