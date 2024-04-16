#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (req, res) => {
  const characters = JSON.parse(res.body).characters;
  for (const character of characters) {
    request(character, (req, res) => {
      console.log(JSON.parse(res.body).name);
    });
  }
});
