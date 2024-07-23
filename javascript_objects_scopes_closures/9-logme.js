#!/usr/bin/node
// Prints new argument value and # of existing

exports.logMe = function (item) {
    if (typeof this.count === 'undefined') {
     this.count = 0;
    }
    console.log(this.count + ': ' + item);
    this.count++;
 };
