#!/usr/bin/node
const request = require('request');
const getCharacters = new Promise((resolve, reject) => {
  request.get(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`,
    (err, response, body) => {
      if (!err) {
        try {
          resolve(JSON.parse(body).characters);
        } catch (error) {
          reject(error);
        }
      }
      reject(err);
    }
  );
});

getCharacters.then((characters) => {
  const arrOfChars = [];
  for (const character of characters) {
    arrOfChars.push(new Promise((resolve, reject) => {
      request(character, (err, response, body) => {
        if (err) reject(err);
        try {
          resolve(JSON.parse(body).name);
        } catch (error) {
          reject(error);
        }
      });
    }));
  }
  Promise.all(arrOfChars).then((chars) => {
    chars.forEach((e) => console.log(e));
  });
});
