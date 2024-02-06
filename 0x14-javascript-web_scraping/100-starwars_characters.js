#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiUrl, (error, response, body) => {
  if (!error) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request.get(characterUrl, (err, res, charBody) => {
        if (!err && res.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error(`Error: ${err}`);
        }
      });
    });
  } else {
    console.error(`Error: ${error}`);
  }
});
