#!/usr/bin/node

// Star Wars Characters

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  const promises = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request(character, (error, resp, bodd) => {
        if (error) {
          console.error(error);
          reject(error);
          return;
        }
        const dat = JSON.parse(bodd);
        resolve(dat.name);
      });
    });
  });
  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error(error);
    });
});
