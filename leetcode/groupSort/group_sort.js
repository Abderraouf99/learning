/**
 * Method to sort an array into a 2D array with frequency
 * @param {*} arr
 * @returns {Array<Array>}
 */
function groupSort(arr) {
  const valueFrequencyMap = new Map();
  for (let value of arr) {
    let currentValueFrequency = valueFrequencyMap.get(value);
    if (currentValueFrequency !== undefined) {
      currentValueFrequency++;
      valueFrequencyMap.set(value, currentValueFrequency);
    } else {
      valueFrequencyMap.set(value, 1);
    }
  }
  const valueFrequencyArray = [];
  valueFrequencyMap.forEach((value, key) => {
    valueFrequencyArray.push([key, value]);
  });
  valueFrequencyArray.sort((a, b) => {
    if (a[1] == b[1] && a[0] < b[0]) {
      return -1;
    } else if (a[1] < b[1]) {
      return 1;
    } else {
      return 0;
    }
  });

  return valueFrequencyArray;
}

const arr = [3, 3, 1, 2, 1];
const expectedValue = [
  [1, 2],
  [3, 2],
  [2, 1],
];
const result = groupSort(arr);
console.log("result: ", result);
console.log("expected value: ", expectedValue);
