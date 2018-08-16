/**
 * Matrix columns are sorted in increasing order
 * The first item in each row is greater than the last item in the previous row
 * algo:
 *  1. Locate the correct row by halfing successively
 *  2. Locate the item in row by halfing successively
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
 * @param {number} range
 * @param {T} target
 * @param {(num: number) => T} getValue
 */
const binarySearch = (range, target, getValue) => {
  let low = 0
  let high = range;
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