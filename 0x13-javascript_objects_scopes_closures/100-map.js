#!/usr/bin/node


// Import the list from 100-data.js
const { list } = require('./100-data'); // Make sure the relative path is correct

// Compute the new list by multiplying each value by its index
const newList = list.map((value, index) => value * index);

// Print the original list and the new list
console.log(list);
console.log(newList);
