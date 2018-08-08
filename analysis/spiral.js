const SPIRAL_DIRECTIONS = [[0, 1] /* E */, [1, 0] /* N */, [0, -1] /* W */, [-1, 0] /* S */];

/**
 * Takes a number n and builds an n x n matrix with n * n numbers filled in with a spiral pattern
 * @param {number} size 
 * @return {Array<Array<number>>} 
 * @example 
 *    printFIFO(spiral(3));
 * 
 *    1 2 3
 *    8 9 4
 *    7 6 5
 */
const spiral = size => {
  let coord = [0, 0];
  const matrix = generateMatrixOfSize(size);
  const shouldTurn = ({0:x, 1:y}) => x < 0 || y < 0 || x === size || y === size || matrix[x][y] !== undefined;
  const compass = makeCompass(SPIRAL_DIRECTIONS, shouldTurn);
  const entries = size * size;
  for (let entry = 1; entry <= entries; entry++) {
    matrix[coord[0]][coord[1]] = entry;
    coord = compass(coord);
  }
  return matrix;
};

/**
 * 
 * @param {Array<Array<number>>} matrix
 * @returns {string} 
 */
const printFIFO = matrix => matrix.map(row => row.join(' ')).join('\n');

/**
 * 
 * @param {Array<Tuple>} directions
 * @param {(i: num) => boolean} shouldTurn
 * @private 
 */
const makeCompass = (directions, shouldTurn) => {
  let dir = 0;
  return (coord) => {
    let next = addTuples(coord, directions[dir]);
    if (shouldTurn(next)) {
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

console.log('spiral \n' + printFIFO(spiral(3)));
console.log('spiral \n' + printFIFO(spiral(4)));