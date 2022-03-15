const MAZE_1 = [
  [1, 5, 0, 0, 0],
  [0, 5, 0, 5, 5],
  [0, 5, 0, 0, 0],
  [0, 5, 0, 5, 0],
  [0, 0, 0, 5, 9],
];

type Maze = typeof MAZE_1;
type Matrix<T> = T[][];
type Cooridinate = readonly [number, number];
type Path = Set<string>;
type Visited = Set<string>;

const navigateMazeDFS = (maze: Maze): Path | undefined => {
  const visited: Visited = new Set();
  const [xBoundary, yBoundary] = getDimensions(maze);

  const search = (coordinate: Cooridinate, path: Path): Path | undefined => {
    if (isVisited(visited, coordinate)) {
      return;
    }
    setVisited(visited, coordinate);

    const value = getValue(maze, coordinate);
    if (value === 5) {
      return;
    }
    if (value === 9) {
      path.add(hashCoordinate(coordinate));
      return path;
    }

    path.add(hashCoordinate(coordinate));

    const nextCoordinates = get3by3SquareAt(coordinate, [xBoundary, yBoundary]);
    for (const nextCoordinate of nextCoordinates) {
      const result = search(nextCoordinate, new Set(path));
      if (result !== undefined) {
        return result;
      }
    }
  };

  return search([0, 0], new Set());
};

const navigateMazeBFS = (maze: Maze): Cooridinate | undefined => {
  const visited: Visited = new Set();
  const [xBoundary, yBoundary] = getDimensions(maze);

  const queue = Queue<Cooridinate>();
  queue.enqueue([0, 0]);

  while (!queue.isEmpty()) {
    const coordinate = queue.dequeue() as Cooridinate;
    if (isVisited(visited, coordinate)) {
      continue;
    }
    setVisited(visited, coordinate);

    const value = getValue(maze, coordinate);
    if (value === 9) {
      return coordinate;
    }
    if (value === 5) {
      continue;
    }

    const nextCoordinates = get3by3SquareAt(coordinate, [xBoundary, yBoundary]);
    for (const nextCoordinate of nextCoordinates) {
      queue.enqueue(nextCoordinate);
    }
  }
};

const get3by3SquareAt = ([x, y]: Cooridinate, [xBoundary, yBoundary]: Cooridinate): Cooridinate[] => {
  const coordinates: Cooridinate[] = [];
  for (let xOffset = -1; xOffset <= 1; xOffset++) {
    for (let yOffset = -1; yOffset <= 1; yOffset++) {
      const cX = x + xOffset;
      const cY = y + yOffset;
      if (cX < 0 || cY < 0 || cX >= xBoundary || cY >= yBoundary) {
        continue;
      }
      coordinates.push([cX, cY]);
    }
  }
  return coordinates;
};

const getValue = <T>(matrix: Matrix<T>, [x, y]: Cooridinate): T => matrix[y][x];
const setValue = <T>(matrix: Matrix<T>, [x, y]: Cooridinate, value: T) => (matrix[y][x] = value);

const isVisited = (visited: Visited, coordinate: Cooridinate): boolean => visited.has(hashCoordinate(coordinate));

const setVisited = (visited: Visited, coordinate: Cooridinate): Visited => visited.add(hashCoordinate(coordinate));

const hashCoordinate = ([x, y]: Cooridinate): string => `${x}:${y}`;

const getDimensions = <T>(matrix: Matrix<T>) => {
  const xBoundary = matrix[0].length;
  const yBoundary = matrix.length;
  return [xBoundary, yBoundary] as const;
};

const buildMatrixFromPath = (path: Path = new Set(), [xBoundary, yBoundary]: Cooridinate): Matrix<number> => {
  const matrix: Matrix<number> = [];
  for (let y = 0; y < yBoundary; y++) {
    matrix.push([]);
    for (let x = 0; x < xBoundary; x++) {
      const value = path.has(hashCoordinate([x, y])) ? 1 : 0;
      setValue(matrix, [x, y], value);
    }
  }
  return matrix;
};

const printMatrix = <T>(matrix: Matrix<T>) => {
  const [xBoundary, yBoundary] = getDimensions(matrix);
  for (let y = 0; y < yBoundary; y++) {
    for (let x = 0; x < xBoundary; x++) {
      const value = getValue(matrix, [x, y]);
      process.stdout.write(`${value}, `);
    }
    process.stdout.write("\n");
  }
};

const Queue = <T>() => {
  const array: T[] = [];
  return {
    enqueue: (item: T) => array.push(item),
    dequeue: (): T | undefined => array.shift(),
    isEmpty: (): boolean => array.length === 0,
  };
};

// console.log(navigateMazeBFS(MAZE_1));
console.log(printMatrix(buildMatrixFromPath(navigateMazeDFS(MAZE_1), getDimensions(MAZE_1))));
console.log(printMatrix(MAZE_1));
