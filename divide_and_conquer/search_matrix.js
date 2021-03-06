/**
 * Matrix columns are sorted in increasing order
 * The first item in each row is greater than the last item in the previous row
 * algo:
 *  1. Binary search through matrix translating item number into x, y coordinates
 * @param {Array<Array<number>>} matrix
 * @param {number} target
 * @returns {boolean}
 */
const searchMatrix = (matrix, target) => {
  const length = matrix.length;
  return binarySearch(length * length, target, n => {
    const row = intDiv(n - 1, length);
    const column = (n - 1) % length;
    return matrix[row][column];
  });
};

/**
 * Algo:
 *  1. split range into [low, mid) & [mid, high)
 *  2. if target == getValue(mid), return true
 *  3. if target < getValue(mid), alg([low, mid])
 *  4. else, algo([mid, high))
 *  5. loop until range == 1
 *  5. return target == getValue(mid)
 * @param {number} numOfItems
 * @param {T} target
 * @param {(nthItem: number) => T} getValue
 */
const binarySearch = (numOfItems, target, getValue) => {
  let low = 1;
  let high = numOfItems;
  let mid;
  while (low < high) {
    mid = intDiv(high + low, 2);
    const midpoint = getValue(mid);
    if (midpoint === target) {
      return true;
    }
    if (target < midpoint) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  return target === getValue(mid);
};

const intDiv = (num, den) => Math.floor(num/den);

module.exports.binarySearch = binarySearch;
module.exports.searchMatrix = searchMatrix;