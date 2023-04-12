#!/usr/bin/node
const variable = process.argv[2];
if (variable === undefined) {
  console.log('No argument');
} else {
  console.log(variable);
}
