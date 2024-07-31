#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', response.statusCode);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).characters;
    for (let i = 0; i < films.length; i++) {
      request.get(films[i], (error, response, body) => {
        if (error) {
          console.log('Error:', response.statusCode);
        } else if (response.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        } else {
          console.error('Failed to fetch the webpage', response.statusCode);
        }
      });
    }
  } else {
    console.error('Failed to fetch the webpage', response.statusCode);
  }
});
