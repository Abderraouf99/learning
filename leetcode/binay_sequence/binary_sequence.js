function countBinarySubStrings(s) {
  let numberOfBinarySubStrings = 0;
  let currentReading = s[0];
  for (let i = 0; i < s.length - 1; i++) {
    const currentValue = s[i];
    const nextValue = s[i + 1];
    if (currentValue !== nextValue) {
      numberOfBinarySubStrings++;
      while (currentReading.length > 1) {
        const upComingSubStr = s.substring(
          i + 1,
          i + 1 + currentReading.length
        );

        if (
          (!upComingSubStr.includes("1") && currentReading.includes("1")) ||
          (!upComingSubStr.includes("0") && currentReading.includes("0"))
        ) {
          if (upComingSubStr.length === currentReading.length)
            numberOfBinarySubStrings++;
        }
        currentReading = currentReading.slice(0, currentReading.length - 1);
      }
      currentReading = nextValue;
    } else {
      currentReading += nextValue;
    }
  }
  return numberOfBinarySubStrings;
}

const returnValue = countBinarySubStrings("00110");
console.log("expected ", 3);
console.log("actual ", returnValue);
