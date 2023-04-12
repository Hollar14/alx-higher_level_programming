#!/usr/bin/node
let numba = process.argv[2];
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < numba; a++) {
    console.log('C is fun');
  }
}
