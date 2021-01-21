// 리스트에서 value를 이진 탐색으로 찾고 인덱스와 찾은 여부 반환
const binarySearch = (li, value) => {
	let n = li.length;
	let left = 0;
	let right = n - 1;
	while (left <= right) {
		let mid = parseInt((left + right) / 2);
		if (li[mid] >= value) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	let found = li[left] === value;
	return [left, found];
};

// 파이썬의 bisect_left 구현 함수
const bisectLeft = (li, value) => {
	const [index, found] = binarySearch(li, value);
	return index;
};

// 파이썬의 bisect_right 구현 함수
const bisectRight = (li, value) => {
	const [index, found] = binarySearch(li, value);
	if (found) return index + 1;
	else return index;
};

// 리스트에서 범위가 [leftValue, rightValue]인 데이터의 개수를 반환하는 함수
const countByRange = (li, leftValue, rightValue) => {
	let rightIndex = bisectRight(li, rightValue);
	let leftIndex = bisectLeft(li, leftValue);
	return rightIndex - leftIndex;
};