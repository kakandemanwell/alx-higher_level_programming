#!/usr/bin/node

let argcount = 0;

exports.logMe = function count (item) {
    console.log(`${argcount} : ${item}`);
    argcount++;
}
