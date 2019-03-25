import {
    getFactorial,
    binomicalCoefficient,
    latticePaths
} from './problem'

it('should calculate the factorial of a number', () => {
    expect(getFactorial(4)).toEqual(24)
    expect(getFactorial(20)).toEqual(2432902008176640000)
})

it('should calculate the binomical coefficient', () => {
    expect(binomicalCoefficient(4,2)).toEqual(6)
    expect(binomicalCoefficient(6,3)).toEqual(20)
    expect(binomicalCoefficient(40,20)).toEqual(137846528820)
})

it ('should get the lattice paths of a grid', () => {
    expect(latticePaths(2)).toEqual(6)
    expect(latticePaths(20)).toEqual(137846528820)
})