export const isDivisor = (number, divisor) => {
    return number % divisor == 0
}

export const isPrime = (number) => {
    if (number < 2) {
        return false
    }
    for (let divisor = 2; divisor < parseInt(number**0.5) + 1; divisor++) {        
        if (isDivisor(number, divisor)) {
            return false
        }
    }
    return true
}

export const getNextPrimeNumber = (currentPrime) => {
    currentPrime = currentPrime + 1  
    while (isPrime(currentPrime) === false) {
        currentPrime = currentPrime + 1
    }
    return currentPrime
}

export const generateNextPrimeNumber = function * (startPrime) {    
    let currentPrime = startPrime   
    while (true) {
        currentPrime = getNextPrimeNumber(currentPrime)
        yield currentPrime
    } 
}

export const getPrimesSum = (maxValue) => {
    let currentPrime = 2
    let acc = 0
    let primeGenerator = generateNextPrimeNumber(currentPrime)
    while (currentPrime < maxValue) {
        acc = acc + currentPrime
        currentPrime = primeGenerator.next().value        
    }
    return acc
}