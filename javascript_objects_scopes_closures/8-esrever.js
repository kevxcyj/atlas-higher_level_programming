#!/usr/bin/node
// Returns reversed version of list

exports.esrever = function (list) {
  const reversedList = [];
  const last = list.length - 1;
  for (let i = last; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
