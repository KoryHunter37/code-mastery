
// https://www.codewars.com/kata/total-amount-of-points/train/go

package kata

func Points(games []string) int {
  total := 0
  
  for _, s := range games{
    x, y := int(s[0]), int(s[2])
    
    if x > y {
    total += 3
    } else if x == y {
    total += 1
    }
  }
  
  return total
}
