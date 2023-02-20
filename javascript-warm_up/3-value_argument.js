#!/usr/bin/node
a = process.argv[2]
if (typeof a === 'undefined'){
    console.log('No argument');
}
else{
    console.log(a);
}
