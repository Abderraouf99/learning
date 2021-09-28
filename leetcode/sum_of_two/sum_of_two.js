/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let returnValue = new ListNode();
  let firstHead = l1;
  let secondHead = l2;
  let currentHead = returnValue;
  let overflow = 0;
  while (firstHead !== null || secondHead !== null) {
    const firstValue = firstHead !== null ? firstHead.val : 0;
    const secondValue = secondHead !== null ? secondHead.val : 0;
    const sum = firstValue + secondValue + overflow;
    overflow = Math.trunc(sum / 10);
    currentHead.next = new ListNode(Math.trunc(sum % 10));
    currentHead = currentHead.next;
    if (firstHead !== null) firstHead = firstHead.next;
    if (secondHead !== null) secondHead = secondHead.next;
  }
  if (overflow > 0) {
    currentHead.next = new ListNode(overflow);
  }
  return returnValue.next;
};

function buildListNodeFromArray(array) {
  let linkedList = new ListNode();
  let currentList = linkedList;
  for (let i = 0; i < array.length; i++) {
    currentList.next = new ListNode(array[i]);
    currentList = currentList.next;
  }
  return linkedList.next;
}
