// https://www.codewars.com/kata/beginner-lost-without-a-map/train/go

package kata

func Maps(x []int) []int {

  y := make([]int, len(x))

  for i := 0; i < len(x); i++{
    y[i] = x[i] * 2
  }
  return y
}
