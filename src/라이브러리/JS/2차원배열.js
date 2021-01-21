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

let rotated = rotateMatrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]);
console.log(rotated);
