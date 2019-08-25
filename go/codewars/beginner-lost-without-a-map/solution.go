// https://www.codewars.com/kata/beginner-lost-without-a-map/train/go

package kata

func Maps(x []int) (y []int) {
  for _, j := range x{
    y = append(y, j*2)
  }
  return y
}
