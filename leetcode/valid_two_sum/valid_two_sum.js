const nums = [3, 2, 4];
const target = 6;

function twoSum(nums, target) {
  let validIndexes = [];
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    const indexOfDiff = nums.indexOf(diff);
    if (indexOfDiff > -1 && indexOfDiff !== i) {
      const secondsNumIndex = nums.indexOf(diff);
      validIndexes.push(i);
      validIndexes.push(secondsNumIndex);
      break;
    }
  }
  return validIndexes;
}

const result = twoSum(nums, target);
const expectedValue = [1, 2];
console.log("Your response is : ", result, "and it should be", expectedValue);
