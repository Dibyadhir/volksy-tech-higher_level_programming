#!/usr/bin/node
const x =  Number.parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  for (i = 0; i < x; i++) {
    console.log('C is fun')
  }
}
