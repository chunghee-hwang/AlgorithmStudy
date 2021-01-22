const stringifyKey = (arr) => JSON.stringify(arr);

const parseKeys = (answer) => Array.from(answer).map((a) => JSON.parse(a));

const keyInAnswer = (arr, answer) => answer.has(stringifyKey(arr));

const possible = (answer) => {
  for (let [x, y, stuff] of parseKeys(answer)) {
    if (stuff === 0) {
      if (
        y === 0 ||
        keyInAnswer([x - 1, y, 1], answer) ||
        keyInAnswer([x, y, 1], answer) ||
        keyInAnswer([x, y - 1, 0], answer)
      ) {
        continue;
      }
      return false;
    } else if (stuff === 1) {
      if (
        keyInAnswer([x, y - 1, 0], answer) ||
        keyInAnswer([x + 1, y - 1, 0], answer) ||
        (keyInAnswer([x - 1, y, 1], answer) &&
          keyInAnswer([x + 1, y, 1], answer))
      ) {
        continue;
      }
      return false;
    }
  }
  return true;
};

function solution(n, build_frame) {
  let answer = new Set();
  for (let frame of build_frame) {
    let [x, y, stuff, operate] = frame;
    const key = stringifyKey([x, y, stuff]);
    if (operate === 0) {
      answer.delete(key);
      if (!possible(answer)) {
        answer.add(key);
      }
    } else if (operate === 1) {
      answer.add(key);
      if (!possible(answer)) {
        answer.delete(key);
      }
    }
  }
  answer = parseKeys(answer).sort((ans, ans2) => {
    const [x, y, a] = ans;
    const [x2, y2, a2] = ans2;

    if (x === x2) {
      if (y === y2) {
        return a - a2;
      } else {
        return y - y2;
      }
    } else {
      return x - x2;
    }
  });
  return answer;
}

solution(5, [
  [1, 0, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 0, 1],
  [2, 2, 1, 1],
  [5, 0, 0, 1],
  [5, 1, 0, 1],
  [4, 2, 1, 1],
  [3, 2, 1, 1],
]);

solution(5, [
  [0, 0, 0, 1],
  [2, 0, 0, 1],
  [4, 0, 0, 1],
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 1],
  [3, 1, 1, 1],
  [2, 0, 0, 0],
  [1, 1, 1, 0],
  [2, 2, 0, 1],
]);
