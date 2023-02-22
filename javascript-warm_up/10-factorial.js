#!/usr/bin/node
const x = Number.parseInt(process.argv[2]);
function fact (num) {
    if (num === 0 || isNaN(num)) {
        return 1;
  } else {
      return num * fact(num - 1);
  }
}
console.log(fact(x));
