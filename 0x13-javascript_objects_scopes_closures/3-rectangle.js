#!/usr/bin/node

class Rectangle{
    constructor(w, h) {
        if (typeof(w) === "number" && w > 0 && Number.isInteger(w) && typeof(h) === "number" && h > 0 && Number.isInteger(h)) {
            this.width = parseInt(w);
            this.height = parseInt(h);
    } else {}
    }

    print() {
        for (let index = 0; index < this.height; index++) {
            let myVar = '';
            let n = 0;
            while (n < this.width) {
                myVar += "X";
                n++
            }
            console.log(myVar)            
        }
    }
}

module.exports = Rectangle;
