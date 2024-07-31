#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch film data:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;
  const characterNames = new Array(characters.length);
  let completedRequests = 0;

  characters.forEach((characterUrl, index) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode === 200) {
        characterNames[index] = JSON.parse(body).name;
      } else {
        console.error('Failed to fetch character data:', response.statusCode);
      }

      completedRequests++;
      if (completedRequests === characters.length) {
        characterNames.forEach(name => {
          if (name) console.log(name);
        });
      }
    });
  });
});
