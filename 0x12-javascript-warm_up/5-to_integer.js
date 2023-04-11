#!/usr/bin/node
if (process.argv[3] === undefined || isNaN(process.argv[3])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[3]));
}

