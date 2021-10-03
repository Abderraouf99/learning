/**
 * Function to get the longest prefix
 * @param {Array<String>} strs
 */
function longestPrefix(strs) {
  let commonPrefix = strs[0];
  for (let j = 1; j <= strs.length - 1; j++) {
    const word = strs[j];
    if (word === "") return "";
    const currentWordLength = word.length; // 4
    const currentCommonPrefixLength = commonPrefix.length; //6
    if (currentWordLength > currentCommonPrefixLength) {
      for (let i = 0; i < currentCommonPrefixLength; i++) {
        if (word[i] !== commonPrefix[i]) {
          commonPrefix = commonPrefix.slice(0, i);
          break;
        }
      }
    } else {
      for (let i = 0; i < currentWordLength; i++) {
        if (word[i] !== commonPrefix[i]) {
          commonPrefix = commonPrefix.slice(0, i);
          break;
        }
        if (i === currentWordLength - 1) {
          commonPrefix = word;
        }
      }
    }
  }
  return commonPrefix;
}

const testInputs = [
  ["flower", "flow", "flight"],
  ["ab", "a"],
  ["ab", "a", ""],
];
const expectedOutPut = ["fl", "a", ""];
testInputs.forEach((inputArray, index) => {
  const actualValue = longestPrefix(inputArray);
  if (actualValue === expectedOutPut[index]) {
    console.log("\x1b[32m", "Correct");
  } else {
    console.log("\x1b[31m", "Wrong");
  }
});
