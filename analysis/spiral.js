const DIRECTIONS = [[0, 1] /* E */, [1, 0] /* N */, [0, -1] /* W */, [-1, 0] /* S */];

/**
 * Takes a number n and builds an n x n matrix with n * n numbers filled in with a spiral pattern
 * @param {number} size 
 * @return {Array<Array<number>>} 
 * @example 
 *    print(spiral(3));
 * 
 *    1 2 3
 *    8 9 4
 *    7 6 5
 */
const spiral = size => {
  let coord = [0, 0];
  const matrix = generateMatrixOfSize(size);
  const compass = makeCompass(size, DIRECTIONS);
  const entries = size * size;
  for (let entry = 1; entry <= entries; entry++) {
    matrix[coord[0]][coord[1]] = entry;
    coord = compass(matrix, coord);
  }
  return matrix;
};

/**
 * 
 * @param {Array<Array<number>>} matrix
 * @returns {string} 
 */
const print = matrix => matrix.map(row => row.join(' ')).join('\n');

/**
 * 
 * @param {number} boundary 
 * @param {Array<Tuple>} directions
 * @private 
 */
const makeCompass = (boundary, directions) => {
  let dir = 0;
  const isOutOfBounds = i => i < 0 || i === boundary;
  return (matrix, coord) => {
    let next = addTuples(coord, directions[dir]);
    if (isOutOfBounds(next[0]) || isOutOfBounds(next[1]) || matrix[next[0]][next[1]] !== undefined) {
      dir = (dir + 1) % directions.length;
      next = addTuples(coord, directions[dir]);
    }
    return next;
  }
}

/**
 * GENERIC HELPERS
 */

const addTuples = (t1, t2) => t1.map((val, i) => val + t2[i]);
const generateMatrixOfSize = s => Array.from(Array(s)).map(() => Array.from(Array(s)));

/**
 * TEST
 */

console.log('spiral \n' + print(spiral(3)));