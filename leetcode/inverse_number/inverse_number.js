const num = 1534236469;
const expectedValue = 0;

const loweBound32Bits = -2147483648;
const higherBound32Bits = 2147483647;

function inverseNumber(x) {
  if (!is32Bits(x)) return 0;
  let stringNumber = x.toString();
  let isSigned = false;
  let returnString = "";
  for (let i = stringNumber.length - 1; i >= 0; i--) {
    const currentChar = stringNumber.charAt(i);
    if (currentChar === "-") {
      isSigned = true;
    }
    returnString = returnString.concat(currentChar);
  }

  let value = parseInt(returnString, 10);
  if (isSigned) {
    value *= -1;
  }
  if (!is32Bits(value)) return 0;
  return value;
}

function is32Bits(value) {
  return value >= loweBound32Bits && value <= higherBound32Bits;
}
/**
 *
 */
const actualValue = inverseNumber(num);
console.log("the actual value is", actualValue);
console.log("You answer is ", actualValue === expectedValue);
