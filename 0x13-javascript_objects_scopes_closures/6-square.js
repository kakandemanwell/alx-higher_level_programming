#!/usr/bin/node

const square = require('./5-square');

class Square extends square{
    charPrint(c) {
        const char = c || "X";

        for (let index = 0; index < this.height; index++) {
            console.log(char.repeat(this.width))
        }
    }
}

module.exports = Square;
