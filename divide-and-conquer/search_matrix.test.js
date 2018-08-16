const {binarySearch, searchMatrix} = require( './search_matrix');


let m = [[1,4,5], [5,7,9], [10,12,67]];

console.log('searchMatrix 4', searchMatrix(m, 4));
console.log('searchMatrix 5', searchMatrix(m, 5));
console.log('searchMatrix 6', searchMatrix(m, 6));
console.log('searchMatrix 9', searchMatrix(m, 9));
console.log('searchMatrix 10', searchMatrix(m, 10))
console.log('searchMatrix 12', searchMatrix(m, 12))
console.log('searchMatrix 56', searchMatrix(m, 56));
console.log('searchMatrix 90', searchMatrix(m, 90));

const arr = [1,2,4,5];

console.log(binarySearch(arr.length, 1, n => arr[n]));
console.log(binarySearch(arr.length, 2, n => arr[n]));
console.log(binarySearch(arr.length, 3, n => arr[n]));
console.log(binarySearch(arr.length, 4, n => arr[n]));
console.log(binarySearch(arr.length, 5, n => arr[n]));