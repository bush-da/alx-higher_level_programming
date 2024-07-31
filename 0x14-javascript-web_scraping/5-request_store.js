#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.log('error ', response.statusCode);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error('Error writing to file', error);
      }
    });
  } else {
    console.log('failed to parse the website', response.statusCode);
  }
});
