#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return (result);
}

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

if (!isNaN(x) && !isNaN(y)) {
  console.log(add(x, y));
} else {
  console.log(NaN);
}
