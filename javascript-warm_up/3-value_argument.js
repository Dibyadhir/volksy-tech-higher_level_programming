#!/usr/bin/node
const a = process.argv[2];
if (typeof a === 'undefined') {
  console.log('No argument');
}else {
  console.log(a);
}
