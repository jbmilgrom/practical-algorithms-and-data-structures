const MAZE_1 = [
  [1, 5, 0, 0, 0],
  [0, 5, 0, 5, 5],
  [0, 5, 0, 0, 0],
  [0, 5, 0, 5, 0],
  [0, 0, 0, 5, 9],
];

type Maze = typeof MAZE_1;

type Cooridinate = [number, number];

type Visited = Set<string>;

const navigateMazeDFS = (maze: Maze): Cooridinate | undefined => {
  const visited: Visited = new Set();
  const xBoundary = maze[0].length;
  const yBoundary = maze.length;

  const search = (coordinate: Cooridinate): Cooridinate | undefined => {
    if (isVisited(visited, coordinate)) {
      return;
    }
    setVisited(visited, coordinate);

    const value = getValue(maze, coordinate);
    if (value === 5) {
      return;
    }
    if (value === 9) {
      return coordinate;
    }

    const nextCoordinates = get3by3SquareAt(coordinate, [xBoundary, yBoundary]);
    for (const nextCoordinate of nextCoordinates) {
      const result = search(nextCoordinate);
      if (result !== undefined) {
        return result;
      }
    }
  };

  return search([0, 0]);
};

const navigateMazeBFS = (maze: Maze): Cooridinate | undefined => {
  const visited: Visited = new Set();
  const xBoundary = maze[0].length;
  const yBoundary = maze.length;

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

const getValue = (maze: Maze, [x, y]: Cooridinate) => maze[y][x];

const isVisited = (visited: Visited, coordinate: Cooridinate): boolean => visited.has(getVisitedKey(coordinate));

const setVisited = (visited: Visited, coordinate: Cooridinate): Visited => visited.add(getVisitedKey(coordinate));

const getVisitedKey = ([x, y]: Cooridinate): string => `${x}:${y}`;

const Queue = <T>() => {
  const array: T[] = [];
  return {
    enqueue: (item: T) => array.push(item),
    dequeue: (): T | undefined => array.shift(),
    isEmpty: (): boolean => array.length === 0,
  };
};

console.log(navigateMazeDFS(MAZE_1));
console.log(navigateMazeBFS(MAZE_1));
