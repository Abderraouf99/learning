const numberToRoman = new Map([
  [1, "I"],
  [4, "IV"],
  [5, "V"],
  [9, "IX"],
  [10, "X"],
  [40, "XL"],
  [50, "L"],
  [90, "XC"],
  [100, "C"],
  [400, "CD"],
  [500, "D"],
  [900, "CM"],
  [1000, "M"],
]);
function intToRoman(num) {
  let remainingValue = num;
  let romanString = "";
  while (remainingValue > 0) {
    if (remainingValue % 1000 !== remainingValue) {
      romanString += numberToRoman.get(1000);
      remainingValue -= 1000;
    } else if (remainingValue % 900 !== remainingValue) {
      romanString += numberToRoman.get(900);
      remainingValue -= 900;
    } else if (remainingValue % 500 !== remainingValue) {
      romanString += numberToRoman.get(500);
      remainingValue -= 500;
    } else if (remainingValue % 400 !== remainingValue) {
      romanString += numberToRoman.get(400);
      remainingValue -= 400;
    } else if (remainingValue % 100 !== remainingValue) {
      romanString += numberToRoman.get(100);
      remainingValue -= 100;
    } else if (remainingValue % 90 !== remainingValue) {
      romanString += numberToRoman.get(90);
      remainingValue -= 90;
    } else if (remainingValue % 50 !== remainingValue) {
      romanString += numberToRoman.get(50);
      remainingValue -= 50;
    } else if (remainingValue % 40 !== remainingValue) {
      romanString += numberToRoman.get(40);
      remainingValue -= 40;
    } else if (remainingValue % 10 !== remainingValue) {
      romanString += numberToRoman.get(10);
      remainingValue -= 10;
    } else if (remainingValue % 9 !== remainingValue) {
      romanString += numberToRoman.get(9);
      remainingValue -= 9;
    } else if (remainingValue % 5 !== remainingValue) {
      romanString += numberToRoman.get(5);
      remainingValue -= 5;
    } else if (remainingValue % 4 !== remainingValue) {
      romanString += numberToRoman.get(4);
      remainingValue -= 4;
    } else {
      romanString += numberToRoman.get(1);
      remainingValue -= 1;
    }
  }
  return romanString;
}

console.log(intToRoman("1880"));
