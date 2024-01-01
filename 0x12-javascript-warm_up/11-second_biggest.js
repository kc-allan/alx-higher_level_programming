#!/usr/bin/node
const nums = process.argv;
if (isNaN(nums[2]) || isNaN(nums[3])) {
  console.log(0);
} else {
  let largest = 0;
  let secLargest = 0;
  for (let i = 2; i < nums.length; i++) {
    const num = parseInt(nums[i]);
    if (num > largest) {
      largest = num;
    }
    for (let k = 2; k < nums.length; k++) {
      const num = parseInt(nums[k]);
      if (num > secLargest && num < largest) {
        secLargest = num;
      }
    }
  }
  console.log(parseInt(secLargest));
}
