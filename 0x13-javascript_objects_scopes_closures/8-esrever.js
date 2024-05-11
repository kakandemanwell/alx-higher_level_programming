#!/usr/bin/node

exports.esrever = function (list) {

    const buffer = [];

    for (index = list.length - 1; index >= 0; index--) {
        buffer.push(list[index]);
    }
    return buffer;
}
