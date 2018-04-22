import { 
  getNumberOfDigitsInNumber, 
  isPalindrome, 
  getLowerRange, 
  productCombinations 
} from './problem'

it('must count the number of digits', () => {
  expect(getNumberOfDigitsInNumber(1234)).toBe(4);
});

it('must check the lower range of a number, it means the lower number before having one digit less', () => {
  expect(getLowerRange(24)).toBe(10)
  expect(getLowerRange(242)).toBe(100)
  expect(getLowerRange(99)).toBe(10)
  expect(getLowerRange(999)).toBe(100)
  expect(getLowerRange(9)).toBe(1)
})

it('must chec if a number is palindrome or not', () => {
  expect(isPalindrome(1221)).toBe(true);
  expect(isPalindrome(12121)).toBe(true);
  expect(isPalindrome(91211219)).toBe(true);
  expect(isPalindrome(12345)).toBe(false);
})

it('must get the hight palindrome value', () => {
  expect(productCombinations(99)).toBe(9009)
  expect(productCombinations(999)).toBe(906609)
})