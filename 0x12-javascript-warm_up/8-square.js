#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let square = '';
    for (let n = 0; n < x; n++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
