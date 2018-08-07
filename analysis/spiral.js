/**
 * 
 * @param {number} size 
 * @return {Array<Array<number>>} 
 */
const spiral = size => {
  let coord = [0, 0];
  const matrix = generateMatrixOfSize(size);
  const getNextCoordinates = makeGetNextCoordintes(size, DIRECTIONS);
  const entries = size * size;
  for (let entry = 1; entry <= entries; entry++) {
    matrix[coord[0]][coord[1]] = entry;
    coord = getNextCoordinates(matrix, coord);
  }
  return matrix;
};

const makeGetNextCoordintes = (size, directions) => {
  let dir = 0;
  const isOutOfBounds = m => m < 0 || m === size;
  return (matrix, coord) => {
    let next = addTuples(coord, directions[dir]);
    if (isOutOfBounds(next[0]) || isOutOfBounds(next[1]) || matrix[next[0]][next[1]] !== undefined) {
      dir = (dir + 1) % directions.length;
      next = addTuples(coord, directions[dir]);
    }
    return next;
  }
}

const DIRECTIONS = [[0, 1] /* E */, [1, 0] /* N */, [0, -1] /* W */, [-1, 0] /* S */];

const addTuples = (t1, t2) => t1.map((val, i) => val + t2[i]);
const generateMatrixOfSize = s => Array.from(Array(s)).map(() => Array.from(Array(s)));

console.log('spiral', spiral(3));