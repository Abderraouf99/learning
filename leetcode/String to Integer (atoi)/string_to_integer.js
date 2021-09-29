const testValue = "   +0 123";
const expectedValue = 0;
function StringToInt(s) {
  let stringToParse = "";
  let hasASign = false;
  for (let i = 0; i < s.length; i++) {
    const currentChar = s.charAt(i);
    if (currentChar === "-" && !hasASign) {
      hasASign = true;
      stringToParse = "-";
    } else if (currentChar === "+" && !hasASign) {
      hasASign = true;
      stringToParse = "+";
    } else if (
      isNaN(currentChar) ||
      (currentChar === " " && stringToParse.length > 0)
    ) {
      return buildNumber(stringToParse);
    } else if (currentChar !== " ") {
      stringToParse = stringToParse.concat(currentChar);
      hasASign = true;
    }
  }
  return buildNumber(stringToParse);
}

function buildNumber(numberStr) {
  const lowerBound32Bits = -2147483648;
  const higherBound32Bits = 2147483647;
  let value = parseInt(numberStr, 10);
  if (isNaN(value)) return 0;
  if (value < lowerBound32Bits) {
    return lowerBound32Bits;
  } else if (value > higherBound32Bits) {
    return higherBound32Bits;
  }
  return value;
}

const actualResult = StringToInt(testValue);
console.log("the actual value returned by the function is \t", actualResult);
console.log("You answer is: ", actualResult === expectedValue);
