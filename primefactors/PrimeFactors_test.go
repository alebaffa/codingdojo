package primeFactors

import "testing"

func getList(num ...int) []int {
	list := []int{}
	for _, value := range num {
		list = append(list, value)
	}
	return list
}

func assertEquals(t *testing.T, list, primeFactors []int) {
	if len(list) != len(primeFactors) {
		t.Error("Error. Expected ", list, ", but it was ", primeFactors)
	}
}

func TestOne(t *testing.T) {
	assertEquals(t, getList(), Generate(1))
}

func TestTwo(t *testing.T) {
	assertEquals(t, getList(2), Generate(2))
}

func TestThree(t *testing.T) {
	assertEquals(t, getList(3), Generate(3))
}

func TestFour(t *testing.T) {
	assertEquals(t, getList(2, 2), Generate(4))
}

func TestSix(t *testing.T) {
	assertEquals(t, getList(2, 3), Generate(6))
}

func TestEight(t *testing.T) {
	assertEquals(t, getList(2, 2, 2), Generate(8))
}

func TestNine(t *testing.T) {
	assertEquals(t, getList(3, 3), Generate(9))
}
