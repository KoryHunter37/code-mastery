// https://www.codewars.com/kata/century-from-year/train/go

package kata

func min(a, b int) int {
  if a < b{
    return a
  }
  return b
}

func century(year int) int {
 return year / 100 + min(1, year%100)
}
