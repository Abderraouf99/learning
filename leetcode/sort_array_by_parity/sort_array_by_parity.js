nums = [3, 1, 4, 2];

function sortArrayByParity(nums) {
  let evenNumbers = [];
  let oddNumbers = [];
  let returnValue = Array(nums.length);
  returnValue.fill(0);
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 === 0) {
      evenNumbers.push(nums[i]);
    } else {
      oddNumbers.push(nums[i]);
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (i % 2 === 0) {
      returnValue[i] = evenNumbers[Math.trunc(i / 2)];
    } else {
      returnValue[i] = oddNumbers[Math.trunc(i / 2)];
    }
  }
  return returnValue;
}

const returnValue = sortArrayByParity(nums);
console.log(returnValue);
