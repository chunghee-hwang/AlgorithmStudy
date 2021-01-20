// https://programmers.co.kr/learn/courses/30/lessons/60059

// 2차원 배열 동적 생성
const createMatrix = (row, column, defaultValue = null) => {
  return Array.from(Array(row), () => Array(column).fill(defaultValue));
};

// 2차원 배열 90도 회전하기
const rotateMatrix = (a) => {
  let n = a.length;
  let m = a[0].length;
  let result = Array.from(Array(m), () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      result[j][n - i - 1] = a[i][j];
    }
  }
  return result;
};

// 자물쇠에 열쇠 삽입
const insertKey = (key, newLock, y, x) => {
  for (let dy = y; dy < y + key.length; dy++) {
    for (let dx = x; dx < x + key.length; dx++) {
      newLock[dy][dx] += key[dy - y][dx - x];
    }
  }
};
// 자물쇠와 열쇠가 일치하는지 확인
const isMatch = (newLock, padding, N) => {
  for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
      if (newLock[y + padding][x + padding] !== 1) return false;
    }
  }
  return true;
};
// 자물쇠에서 열쇠 제거
const removeKey = (key, newLock, y, x) => {
  for (let dy = y; dy < y + key.length; dy++) {
    for (let dx = x; dx < x + key.length; dx++) {
      newLock[dy][dx] -= key[dy - y][dx - x];
    }
  }
};

function solution(key, lock) {
  const M = key.length;
  const N = lock.length;
  const padding = M - 1;
  const newN = N + padding * 2;
  let newLock = createMatrix(newN, newN, 0);
  for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
      newLock[y + padding][x + padding] = lock[y][x];
    }
  }
  for (let rotateCnt = 0; rotateCnt < 4; rotateCnt++) {
    for (let y = 0; y <= newN - M; y++) {
      for (let x = 0; x <= newN - M; x++) {
        insertKey(key, newLock, y, x);
        if (isMatch(newLock, padding, N)) {
          return true;
        }
        removeKey(key, newLock, y, x);
      }
    }
    key = rotateMatrix(key);
  }

  return false;
}

solution(
  [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1],
  ],
  [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
  ]
);
