// https://www.codewars.com/kata/square-n-sum/train/go

package kata

func SquareSum(numbers []int) int {
  total := 0

  for _, element := range numbers{
    total += element * element
  }
  
  return total
}
