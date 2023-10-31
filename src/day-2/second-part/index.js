const fs = require('fs');

let boxes = [];
let total_length = 0;

fs.readFile('./input.txt', 'utf8' , (err, boxes_dimensions_list) => {
    boxes = boxes_dimensions_list.split("\n");
    for (box of boxes){
        var dimensions = box.split("x").map(dimension => Number(dimension));
        var side1 = 2*(dimensions[0]+dimensions[1]);
        var side2 = 2*(dimensions[0]+dimensions[2]);
        var side3 = 2*(dimensions[1]+dimensions[2]);
        total_length += Math.min(side1, side2, side3);
        total_length += dimensions[0]*dimensions[1]*dimensions[2];
    }
    console.log("The elves should order", total_length, "feet of ribbon.");
})
