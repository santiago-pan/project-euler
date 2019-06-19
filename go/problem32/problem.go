package main

import (
	"fmt"
)

func main() {
	solution := solution()
	fmt.Println(solution)
}

func includes(a []int, x int) bool {
	for n := range a {
			if x == n {
				return true
			}
	}
	return false
}

func solution() int {
	var products []int
	var sum int = 0
	var prod int = 0
	var compiled int = 0

	for m := 2; m < 100; m++ {
		var nbegin int = 0
		if m > 9 {
			nbegin = 123
		} else {
			nbegin = 1234
		}
		nend := 10000 / m + 1

		for n := nbegin; n < nend; n++ {
			prod = m * n
			compiled = concat(concat(prod, n), m)
			if (compiled >= 1e8 && compiled < 1e9 && isPandigital(compiled)) {
				if (includes(products, prod) == false) {
					products = append(products, prod)
				}
			}
		}
	}

	for i := 0; i < len(products); i++ {
		sum += products[i]
	}
	return sum
}

func isPandigital(n int) bool {	
	var digits uint = 0
	var count uint = 0
	var tmp uint = 0

	for {
		if (n <=0) {
			break
		}
		tmp = digits;
		digits = digits | 1 << (uint)((n % 10) - 1)
		if (tmp == digits) {
			return false
		}
		count++
		n /= 10
	}
	return digits == (1 << count) - 1	
}

func concat(a int, b int) int {
	c:= b
	for {
		if (c <= 0) {
			break
		}
		a *= 10
		c /= 10
	}
	return a + b
}