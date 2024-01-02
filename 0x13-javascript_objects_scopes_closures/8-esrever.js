#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let index = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[index] = list[i];
    index++;
  }
  return newList;
};
