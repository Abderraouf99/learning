const inputEmail = [
  "test.email+alex@leetcode.com",
  "test.e.mail+bob.cathy@leetcode.com",
  "testemail+david@lee.tcode.com",
];

function filterEmails(emailList) {
  let uniqueEmails = [];
  for (const email of emailList) {
    const splittedEmail = email.split("@");
    let localName = splittedEmail[0];
    if (localNameHasDots(localName)) {
      localName = onHasDotsRemoveDots(localName);
    }
    if (localNameHasPlusSign(localName)) {
      localName = onHasPlusSignIgnoreAfterward(localName);
    }
    const formattedEmail = localName + "@" + splittedEmail[1];
    if (!uniqueEmails.includes(formattedEmail)) {
      uniqueEmails.push(formattedEmail);
    }
  }
  return uniqueEmails.length;
}

function localNameHasDots(localName) {
  return localName.indexOf(".") > -1;
}

function localNameHasPlusSign(localName) {
  return localName.indexOf("+") > -1;
}

function onHasDotsRemoveDots(localName) {
  let newLocalName = "";
  for (const char of localName) {
    if (char !== ".") {
      newLocalName += char;
    }
  }
  return newLocalName;
  // if you are using a newer version of node or browser this will work
  // return localName.replaceAll(".", "");
}
function onHasPlusSignIgnoreAfterward(localName) {
  return localName.split("+")[0];
}

const result = filterEmails(inputEmail);
const expected = 2;
