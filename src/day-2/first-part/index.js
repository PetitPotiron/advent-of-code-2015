const fs = require('fs');

let boxes = [];
let total_square_feet = 0;


fs.readFile('./input.txt', 'utf8' , (err, data) => {
    boxes = data.split("\n").map(value => value.replace('\r', '').split("x").map(value => Number(value)));
    boxes.forEach(box => {
        let lowest = Infinity;
        let dimensions = [box[0]*box[1]*2 , box[1]*box[2]*2, box[0]*box[2]*2];
        for (dimension of dimensions) {
            if (dimension/2 < lowest) {
                lowest = dimension/2;
            }
        }
        dimensions.push(lowest);
        dimensions = dimensions[0] + dimensions[1] + dimensions[2] + dimensions[3];
        total_square_feet += dimensions;
    })
    console.log("The elves should order", total_square_feet, "square feet of wrapping paper.");
})