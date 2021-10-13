/**
 * Function to reorder the logs
 * @param {String[]} logs
 */
function reorderLogFiles(logs) {
  const letterLogs = [];
  const digitLogs = [];
  for (const log of logs) {
    const splittedLog = log.split(" ");
    if (isNaN(splittedLog[1])) {
      letterLogs.push(log);
    } else {
      digitLogs.push(log);
    }
  }
  letterLogs.sort((a, b) => {
    const whiteSpaceIndexA = a.indexOf(" ");
    const whiteSpaceIndexB = b.indexOf(" ");
    const aLog = a.substring(whiteSpaceIndexA + 1);
    const bLog = b.substring(whiteSpaceIndexB + 1);
    const aId = a.substring(0, whiteSpaceIndexA);
    const bId = b.substring(0, whiteSpaceIndexB);
    if (aLog.localeCompare(bLog) === 0) {
      return aId.localeCompare(bId);
    }
    return aLog.localeCompare(bLog);
  });
  return [...letterLogs, ...digitLogs];
}

const logs = [
  "dig1 8 1 5 1",
  "let1 art can",
  "dig2 3 6",
  "let2 own kit dig",
  "let3 art zero",
];

reorderLogFiles(logs);
