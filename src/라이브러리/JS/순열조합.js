/**
 * 조합 구하는 함수
 * @param {any[]} arr 섞을 배열
 * @param {number} size 묶을 수
 */
// https://stackoverflow.com/a/45813619
function getCombinations(arr, size) {
  let result = [];
  function c(t, i) {
    if (t.length === size) {
      result.push(t);
      return;
    }
    if (i + 1 > arr.length) {
      return;
    }
    c(t.concat(arr[i]), i + 1);
    c(t, i + 1);
  }
  c([], 0);
  return result;
}

/**
 * 순열 구하는 함수
 * @param {any[]} arr 섞을 배열
 * @param {number} size 묶을 수
 */
// https://gist.github.com/justinfay/f30d53f8b85a274aee57
function getPermutations(array, size) {
  let n = array.length;
  let indices = [];
  for (let i = 0; i < n; i++) {
    indices.push(i);
  }
  let cycles = [];
  for (let i = n; i > n - size; i--) {
    cycles.push(i);
  }
  let results = [];
  let res = [];
  for (let k = 0; k < size; k++) {
    res.push(array[indices[k]]);
  }
  results.push(res);

  let broken = false;
  while (n > 0) {
    for (let i = size - 1; i >= 0; i--) {
      cycles[i]--;
      if (cycles[i] === 0) {
        indices = indices
          .slice(0, i)
          .concat(indices.slice(i + 1).concat(indices.slice(i, i + 1)));
        cycles[i] = n - i;
        broken = false;
      } else {
        let j = cycles[i];
        let x = indices[i];
        indices[i] = indices[n - j];
        indices[n - j] = x;
        let res = [];
        for (let k = 0; k < size; k++) {
          res.push(array[indices[k]]);
        }
        results.push(res);
        broken = true;
        break;
      }
    }
    if (broken === false) {
      break;
    }
  }
  return results;
}

let array = ['a', 'b', 'c', 'd'];

const permutations = getPermutations(array, 2);
console.log(getPermutations);
