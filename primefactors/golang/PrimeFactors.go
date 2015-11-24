package primeFactors

func Generate(num int) []int {
	primeFactors := []int{}
	for candidate := 2; num > 1; candidate++ {
		for ; num%candidate == 0; num /= candidate {
			primeFactors = append(primeFactors, num)
		}
	}
	return primeFactors
}
