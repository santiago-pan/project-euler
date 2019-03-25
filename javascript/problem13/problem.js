export const getNumberOfDigitsInNumber = function(number) {
    return Math.max(Math.floor(Math.log10(Math.abs(number))), 0) + 1;
}

export const shiftNumberToKeepOnlyNumberOfDigits = (number, numDigits) => {
    return Math.round(number / Math.max(1, 10 ** (getNumberOfDigitsInNumber(number) - numDigits)))
}  

export const getFirstTenDigits = (text) => text.toString().substring(0,10)

export const getArrayFromInput = (input) => input.split('\n').map(number => parseInt(number))

export const sumAllNumbers = (numbers) => numbers.reduce((acc, current) => acc+current, 0)

export const solveProblem = (INPUT) => {
    const input = getArrayFromInput(INPUT)
    const allSum = sumAllNumbers(input)
    const firstTen = shiftNumberToKeepOnlyNumberOfDigits(allSum, 10)
    return firstTen
}