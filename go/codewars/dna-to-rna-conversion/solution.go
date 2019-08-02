// https://www.codewars.com/kata/dna-to-rna-conversion/train/go

package kata

import (
"fmt"
"strings"
)

func DNAtoRNA(dna string) string {
  s := strings.Split(dna, "")
  
  fmt.Printf("%v", s)
  
  for i := range s{
    if s[i] == "T"{
      s[i] = "U"
    }
  }
  
  return strings.Join(s, "")
}
