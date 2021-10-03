/**
 * Function to determine if a number is a palindrome
 * @param {Number} x
 * @returns {Boolean} if the number a palindrome or not
 */
function isPalindromeNumber(x) {
  const numberArray = Array.from(String(x), (num) => Number(num));
  const length = numberArray.length;
  for (let i = 0; i < length; i++) {
    const elementFromTheLeft = numberArray[i];
    const elementFromTheRight = numberArray[length - 1 - i];
    if (elementFromTheLeft !== elementFromTheRight) {
      return false;
    }
    if (i === length - 1 - i) {
      return true;
    }
  }
  return true;
}

const testInputs = [121, -121, 10, -101, 53978, -53978, 94997];
const expectedOutPuts = [true, false, false, false, false, false, false];

testInputs.forEach((input, index) => {
  const actualOutPut = isPalindromeNumber(input);
  const expectedOutPut = expectedOutPuts[index];
  if (actualOutPut === expectedOutPut) {
    console.log("\x1b[32m", "Correct");
  } else {
    console.log("\x1b[31m", "Wrong");
  }
});
