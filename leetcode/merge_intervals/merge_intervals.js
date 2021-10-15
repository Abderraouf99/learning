/**
 * Function to returns all the merged intervals of the intervals param
 * @param {[[]]} intervals
 * @returns
 */
const lowerBound = 0;
const highestBound = 1;
function merge(intervals) {
  const result = [];
  // first we order the array of intervals by the smallest lower bound (ascending according to the lower bound)
  intervals.sort((a, b) => a[lowerBound] - b[lowerBound]);
  let currentInterval = intervals[0]; // setting the current interval to first interval

  for (const interval of intervals) {
    // it means the that the lowest bound of the interval is within the current interval
    if (currentInterval[highestBound] >= interval[lowerBound]) {
      currentInterval[highestBound] = Math.max(
        currentInterval[highestBound],
        interval[highestBound]
      );
    } else {
      // it means we have built the largest possible interval from the current interval
      result.push(currentInterval);
      currentInterval = interval;
    }
  }
  result.push(currentInterval);
  return result;
}

const expected = [
  [1, 6],
  [8, 10],
  [15, 18],
];
const result = merge([
  [1, 3],
  [8, 10],
  [2, 6],
  [15, 18],
]);

console.log("the result is: ", result);
console.log("the expected is: ", expected);
