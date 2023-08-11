#!/usr/bin/node

const arg = process.argv.length - 2;

if (arg === 0) {
  console.log('No Argument');
} else if (arg === 1) {
  console.log('Argument');
} else {
  console.log('Arguments');
}
