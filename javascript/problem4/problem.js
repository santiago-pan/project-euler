// A palindromic number reads the same both ways. 
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

export const getNumberOfDigitsInNumber = function(number) {
    return Math.max(Math.floor(Math.log10(Math.abs(number))), 0) + 1;
}

export const getLowerRange = function (number) {
    const digits = getNumberOfDigitsInNumber(number)
    return Math.pow(10, digits - 1)
}

export const isPalindrome = function (number) {
    let reverse = 0    
    const original = number
    while (number != 0) {
	    let rem = number % 10
	    reverse = reverse * 10 + rem
        number = Math.floor(number / 10)
    }
    if (reverse === original) {     
        return true
    } else {
        return false
    }
}

export const productCombinations = function (number) {
    const lowerRange = getLowerRange(number)
    let leftNumber = number
    let rightNumber = number
    let maxPalindrome = 0

    while (leftNumber > lowerRange && rightNumber > lowerRange) {
        let candidate = leftNumber * rightNumber
        if (isPalindrome(candidate)) {
            if (candidate > maxPalindrome) {
                maxPalindrome = candidate
            }
        }
        leftNumber--
        if (leftNumber == lowerRange) {
            rightNumber--
            leftNumber = number
        }
    }
    return maxPalindrome
}


// 999 x 999

