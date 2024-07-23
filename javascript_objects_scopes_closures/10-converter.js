#!/usr/bin/node
// Converts a number from base 10 to another base

exports.converter = function (base) { return num => num.toString(base); };
