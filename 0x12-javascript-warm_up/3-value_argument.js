#!/usr/bin/node

// prints the first argument passed to it

const arg = process.argv;

if (arg.length < 3) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
