export const getFactorial = (number) => {
    return number === 1 ? number : number * getFactorial(number-1)
}

export const binomicalCoefficient = (n, k) => {
    return getFactorial(n) / (getFactorial(k) * getFactorial(n-k))
}

export const latticePaths = (grid) => {
    let n = grid * 2
    let k = grid
    return binomicalCoefficient(n, k)
}