// https://programmers.co.kr/learn/courses/30/lessons/60062

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

function solution(n, weak, dist) {
  const length = weak.length;
  const friendCount = dist.length;
  let answer = friendCount + 1; // 투입할 친구 수의 최솟값을 찾아야 하므로 dist.length + 1로 초기화
  // 길이를 2배로 늘려서 원형을 일자 형태로 변형하기
  for (let i = 0; i < length; i++) {
    weak.push(weak[i] + n);
  }
  //친구를 나열하는 모든 경우 구하기
  const friendPerm = getPermutations(dist, friendCount);

  // 0 부터 length - 1까지의 위치를 각각 시작점으로 설정
  for (let start = 0; start < length; start++) {
    // 친구를 나열하는 모든 경우 각각에 대하여 확인
    for (let friends of friendPerm) {
      let count = 1; // 투입할 친구의 수
      // 해당 친구가 점검할 수 있는 마지막 위치
      let position = weak[start] + friends[count - 1];
      // 시작점부터 모든 취약한 지점을 확인
      for (let index = start; index < start + length; index++) {
        // 점검할 수 있는 위치를 벗어나는 경우
        if (position < weak[index]) {
          count += 1; // 새로운 친구를 투입
          if (count > friendCount) break; // 더 투입이 불가능하다면 종료
          position = weak[index] + friends[count - 1];
        }
      }
      answer = Math.min(answer, count); // 최솟값 계산
    }
  }
  if (answer > friendCount) return -1;
  return answer;
}

solution(12, [1, 5, 6, 10], [1, 2, 3, 4]);
