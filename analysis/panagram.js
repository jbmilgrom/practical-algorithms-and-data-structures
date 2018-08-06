/**
 * 1. Get Acquainted
 *    *Test whether a given string contains every letter of the alphabet*
 *    A string consists of characters; some may be part of the 26 character alphabet;
 *    we need to determine whether every letter is represented
 * 2. Working for a Better Understanding
 *    condition: a string consisting of consecutive alpha-numeric characters
 *    data: the 26 letter alphabet
 *    uknown: whether the string has every letter of the 26 letter alphabet present
 * 3. Plan 
 *    Create a dictionary of all 26 letters of the alphabet
 *    Iterate through string
 *    Mark letter in dictionary
 *    Iterate through dictionary
 *    Return false if false encountered, true otherwise
 * 4. Looking back
 *    Capture all used characters in a dictionary
 *    Check that every character is used against the 26 letter alphabet
 *    runtime: n + 26, where n is the number of characters in the string
 * @param {string} string 
 * @returns {boolean}
 */
const isPanagram = string => {
  const usedCharacters = {};

  // use a hashmap to optimize for reads in the below ALPHABET.every iteration
  for (let i = 0; i < string.length; i++) {
    usedCharacters[string[i]] = true;
  }

  return ALPHABET.split('').every(char => usedCharacters[char]);
};

const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';

console.log('isPanagram', isPanagram('the quick brown fox jumps over the lazy dog'));
console.log('isPanagram', isPanagram('the quick brown fox jumer the lazy dog'));