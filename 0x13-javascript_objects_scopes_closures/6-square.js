#!/usr/bin/node

const square = require('./5-square');

class Square extends square{
    constructor(size) {
        super(size)
    } 

    charPrint(c) {
        const char = c || "X";

        for (let index = 0; index < this.height; index++) {
            console.log(char.repeat(this.width))
        }
    }
}