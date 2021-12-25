function dec2bin(dec) {
  return (dec >>> 0).toString(2);
}
let numberOfClauses = 5;
console.log("the truth table is \n");
const truthTable = [];
for (let i = 0; i < Math.pow(2, numberOfClauses); i++) {
  const booleanValue = Array.from(dec2bin(i));
  if (booleanValue.length < numberOfClauses) {
    const offset = numberOfClauses - booleanValue.length;
    for (let i = 0; i < offset; i++) {
      booleanValue.unshift("0");
    }
  }
  const p = eval(
    `${booleanValue[0]}&&${booleanValue[1]} || ${booleanValue[2]} && ${booleanValue[3]} || ${booleanValue[4]}`
  );
  booleanValue.push(p);
  truthTable.push(booleanValue);
}
console.log(truthTable);
for (let i = numberOfClauses; i >= 0; i--) {
  const majorClause = i;
  const nextEntryOffset = Math.pow(2, i); // case of i = 0, least significant bit the entry in the table that has the is at 2^{i} position form the current entry
  for (let j = 0; j < truthTable.length; j++) {
    const currentEntry = truthTable[j];
    const nextEntry = truthTable[j + nextEntryOffset];
    if (nextEntry !== undefined) {
      const minorClauseValuesCurrentEntry = currentEntry.splice(majorClause, 1);
      const minorClauseNextEntry = nextEntry.splice(majorClause, 1);
      if (minorClauseNextEntry === minorClauseValuesCurrentEntry) {
        console.log("found similar minor clauses");
      }
    }
  }
}
