function countBinarySequenceFast(s) {
  let count = 0; // count of binary sequences
  let currentCharCounter = 1; // current similar char counter
  let previousCharCounter = 0; // previous similar char counter
  for (let i = 1; i < s.length; i++) {
    if (s[i] === s[i - 1]) {
      currentCharCounter++;
    } else {
      count += Math.min(previousCharCounter, currentCharCounter);
      previousCharCounter = currentCharCounter;
      currentCharCounter = 1;
    }
  }
  count += Math.min(previousCharCounter, currentCharCounter);
  return count;
}

const returnValue = countBinarySequenceFast("00110");
console.log("expected ", 3);
console.log("actual ", returnValue);
