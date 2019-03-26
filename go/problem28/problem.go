package main

import (
	"fmt"
	"math"
)

func ringNSum(n float64) int {
	return int(4*math.Pow(2*n+1, 2) - 12*n)
}

func solution() int {
	acc := 1
	for n := 1; n < 501; n++ {
		acc += ringNSum(float64(n))
	}

	return acc
}

func main() {
	solution := solution()
	fmt.Println(solution)
}
