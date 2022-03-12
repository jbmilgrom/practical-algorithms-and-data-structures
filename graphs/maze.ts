const MAZE_1 = [
  [1, 5, 0, 0, 0],
  [0, 5, 0, 5, 5],
  [0, 5, 0, 0, 0],
  [0, 5, 0, 5, 0],
  [0, 0, 0, 5, 9],
] as const;

type Maze = typeof MAZE_1;

type Cooridinate = [number, number];

type Visited = Set<string>;

const navigateMaze = (maze: Maze): Cooridinate | undefined => {
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

console.log(navigateMaze(MAZE_1));
