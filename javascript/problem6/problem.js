export const createArrayToNumber = (toNumber) => {
    return [...Array(toNumber).keys()].map(k => k + 1)
}

export const sumOfAllNumbers = (number) => number * (number + 1) / 2
export const summOfAllSquareNumbers = (number) => (number * (number + 1) * (2 * number + 1)) / 6

export const getSquareProductsToNumber = (toNumber) => {
    
    const sumSquare = sumOfAllNumbers(toNumber)
    const squareSum = summOfAllSquareNumbers(toNumber)

    return sumSquare * sumSquare - squareSum
}