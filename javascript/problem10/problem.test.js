import { isDivisor, isPrime, getNextPrimeNumber, generateNextPrimeNumber, getPrimesSum } from './problem'

it('should check if a number is divisible by the other', () => {
    expect(isDivisor(10,2)).toEqual(true)
    expect(isDivisor(10,3)).toEqual(false)
})

it('sould check if a number is prime or not', () => {
    expect(isPrime(5)).toBe(true)
    expect(isPrime(17)).toBe(true)
    expect(isPrime(4)).toBe(false)
})

it('should check the get next generator prime function', () => {
    expect(getNextPrimeNumber(5)).toBe(7)
})

it('should check the next prime factor generator', () => {
    let generator = generateNextPrimeNumber(2)
    expect(generator.next().value).toBe(3)
    expect(generator.next().value).toBe(5)
    expect(generator.next().value).toBe(7)
})

it('should check the sum of primes below a max value', () => {
    expect(getPrimesSum(10)).toBe(17)
    //expect(getPrimesSum(2000000)).toBe(142913828922)
})