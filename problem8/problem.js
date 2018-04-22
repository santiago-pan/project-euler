export const getSubString = (inputDigit, fromIndex, ofLength) => {
    return inputDigit.substr(fromIndex, ofLength)
}

export const multiplyDigitsInNumber = (numberString) => {
    return numberString
    .split('')
    .map(number => parseInt(number))
    .reduce((acc, current) => acc * current, 1)
}

export const getMaxMultiplicationValueOfSubstring = (inputDigit, numDigits) => {
    let fromIndex = 0
    let maxValue = 0
    const inputLenght = inputDigit.length

    while (fromIndex < inputLenght - numDigits + 1) {
        let subDigit = getSubString (inputDigit, fromIndex, numDigits)
        const multiplication = multiplyDigitsInNumber(subDigit)
        maxValue = Math.max(maxValue, multiplication)
        fromIndex = fromIndex + 1
    }
    return maxValue
}