// https://www.codewars.com/kata/abbreviate-a-two-word-name/train/go

package kata

import "strings"

func AbbrevName(name string) string{
  names := strings.Split(strings.ToUpper(name), " ")
  return string(names[0][0]) + "." + string(names[1][0])
}
