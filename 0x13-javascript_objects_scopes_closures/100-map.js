#!/usr/bin/node
const theList = require('./100-data.js').list;
console.log(theList);
let times = 0;
const secondList = theList.map(function (x) {
  return (x * times++);
});
console.log(secondList);
