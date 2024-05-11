#!/usr/bin/node

let argcount = 0;

exports.logMe = function (item) {
    console.log(`${argcount} : ${item}`);
    argcount++;
}
