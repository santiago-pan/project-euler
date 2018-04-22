import { 
    createArrayToNumber, 
    getSquareProductsToNumber, 
    sumOfAllNumbers, 
    summOfAllSquareNumbers
} from './problem'
it('must get an array of nombres', () => {
    expect(createArrayToNumber(5)).toEqual([1,2,3,4,5])
})

it('must calculate the sum of all numbers', () => {
    expect(sumOfAllNumbers(10)).toEqual(55)
})

it('must calculate the sum of all square numbers', () => {
    expect(summOfAllSquareNumbers(10)).toEqual(385)
})

it('must get the square products up to a number difference', () => {    
    expect(getSquareProductsToNumber(10)).toEqual(2640)
    expect(getSquareProductsToNumber(100)).toEqual(25164150)
})