function findTarget(arr, target) {
    const len = arr.length;
    for (let i = 0; i < len-1; i++) {
        for (let j = i+1; j < len; j++) {
            if (arr[i] + arr[j] === target) {
                return [i, j];
            }
        }
    }
    return 'Target not found';
}


console.log(findTarget([2, 7, 11, 15], 9)); // # should return [0, 1].
console.log(findTarget([3, 2, 4, 5], 6)); // should return [1, 2].
console.log(findTarget([1, 3, 5, 6, 7, 8], 15)); // should return [4, 5].
console.log(findTarget([1, 3, 5, 7], 14)); // should return 'Target not found'.