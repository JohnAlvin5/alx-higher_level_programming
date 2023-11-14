#!/usr/bin/node
const dictionary = require('./101-data.js').dict;
const reversedDict = {};
for (const key in dictionary) {
  const value = dictionary[key];
  if (reversedDict[value] === undefined) {
    reversedDict[value] = [key];
  } else {
    reversedDict[value].push(key);
  }
}
console.log(reversedDict);
