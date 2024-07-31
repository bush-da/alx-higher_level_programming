#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log('Error: ', response.statusCode);
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log('Failed to fetch the movie ', response.statusCode);
  }
});
