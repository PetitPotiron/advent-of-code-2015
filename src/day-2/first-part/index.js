const fs = require('fs');

let boxes = [];
let total_area = 0;

fs.readFile('./input.txt', 'utf8' , (err, boxes_dimensions_list) => {
    boxes = boxes_dimensions_list.split("\n");
    for (box of boxes){
        var dimensions = box.split("x").map(dimension => Number(dimension));
        var side1 = dimensions[0]*dimensions[1];
        var side2 = dimensions[0]*dimensions[2];
        var side3 = dimensions[1]*dimensions[2];
        total_area += 2*side1
        total_area += 2*side2
        total_area += 2*side3
        total_area += Math.min(side1, side2, side3)
    }
console.log("The elves should order", total_area, "square feet of wrapping paper.");
})
