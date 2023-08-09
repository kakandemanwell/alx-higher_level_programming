#!/usr/bin/node

/*
prints the output depending on the number of
passed arguments
*/

const arg = process.argv.length;

if (arg > 2) {
  console.log('Argument' + (arg > 3 ? 's' : '') + ' found');
} else {
  console.log('Arguments found');
}
