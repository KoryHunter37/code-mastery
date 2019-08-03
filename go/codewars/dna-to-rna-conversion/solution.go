// https://www.codewars.com/kata/dna-to-rna-conversion/train/go

package kata

import "strings"

func DNAtoRNA(dna string) string {
  return strings.ReplaceAll(dna, "T", "U")
}
