/**
 * 1. Check if letter in s1 is in s2
 * 2. if not, return false
 * 3. else, checkoff letter from s2
 * 4. return true
 * @param {string} s1 
 * @param {string} s2 
 */
const isAnagram = (s1, s2) => {
  isCheckedOff = {};
  const { length } = s1;
  if (length !== s2.length) {
    return false;
  }

  for (let i = 0; i < length; i++) {
    const c1 = s1[i];
    let isLetterFound = false
    for (let j = 0; j < length; j++) {
      if (!isCheckedOff[j] && s2[j] === c1) {
        isCheckedOff[j] = true;
        isLetterFound = true;
        break;
      }
    }
    if (!isLetterFound) {
      return false;
    }
  }
  
  return true;
};

console.log(isAnagram('elo', 'leo'));
console.log(isAnagram('elo', 'ley'));

