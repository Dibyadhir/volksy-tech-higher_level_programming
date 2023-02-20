#!/usr/bin/node
a = process.argv
if (a.length == 3){
    console.log("Argument found")
}
else if (a.length > 2){
    console.log("Arguments found")
}
else{
    console.log("No argument")
}
