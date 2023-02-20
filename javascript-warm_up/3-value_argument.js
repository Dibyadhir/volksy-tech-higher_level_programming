#!/usr/bin/node
let a = process.argv[2]
if (typeof a === 'undefined') {
  console.log('No argument');
}
else {
  console.log(a);
}
