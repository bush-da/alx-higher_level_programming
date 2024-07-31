#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const taskReport = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    todos.forEach((task) => {
      if (task.completed) {
        if (Object.prototype.hasOwnProperty.call(taskReport, task.userId)) {
          taskReport[task.userId] += 1;
        } else {
          taskReport[task.userId] = 1;
        }
      }
    });
    console.log(taskReport);
  }
});
