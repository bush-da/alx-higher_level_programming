#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.log('error ', response.statusCode);
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body).results;
    film.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes('/18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  } else {
    console.log('failed to fetch the movie', response.statusCode);
  }
});
