#!/usr/bin/node

const x = process.argv.slice(2);
// console.log(x, typeof x)
if (x.length in [0, 1]) {
  console.log(0);
} else {
  for (const i in x) {
    // console.log(i,typeof i)
    x[i] = Number.parseInt(x[i]);
  }
}
x.sort(function (a, b) { return b - a; });
console.log(x[1]);
