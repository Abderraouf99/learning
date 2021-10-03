/**
 * Function to get the roman number
 * @param {String} s
 * @returns {Number}
 */
const romanNumbersMap = new Map([
  ["I", 1],
  ["V", 5],
  ["X", 10],
  ["L", 50],
  ["C", 100],
  ["D", 500],
  ["M", 1000],
]);
function romanNumber(s) {
  let sum = 0;
  let previousChar = "";
  for (const char of s) {
    const currentCharValue = romanNumbersMap.get(char);
    if (char === "V" && previousChar === "I") {
      sum += 3;
    } else if (char === "X" && previousChar === "I") {
      sum += 8;
    } else if (char === "L" && previousChar === "X") {
      sum += 30;
    } else if (char === "C" && previousChar === "X") {
      sum += 80;
    } else if (char === "D" && previousChar === "C") {
      sum += 300;
    } else if (char === "M" && previousChar === "C") {
      sum += 800;
    } else {
      sum += currentCharValue;
    }
    previousChar = char;
  }
  return sum;
}

const testInputs = ["III", "IV", "IX", "LVIII", "MCMXCIV"];
const expectedOutPuts = [3, 4, 9, 58, 1994];

testInputs.forEach((input, index) => {
  const actualAnswer = romanNumber(input);
  if (expectedOutPuts[index] === actualAnswer) {
    console.log("\x1b[32m", "Correct");
  } else {
    console.log("\x1b[31m", "Wrong");
  }
});
