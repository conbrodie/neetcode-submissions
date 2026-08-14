public class Solution {
    public bool IsAnagram(string s, string t) {
    
       if (s.Length != t.Length) return false; 

        var fistAnagram = new Dictionary<char, int>();
        foreach (var c in s) {
            if (fistAnagram.ContainsKey(c)) {
                fistAnagram[c] += 1;
                continue;
            }

            fistAnagram.Add(c, 1);
        }

        var secondAnagram = new Dictionary<char, int>();
        foreach (var c in t) {
                if (secondAnagram.ContainsKey(c)) {
                    secondAnagram[c] += 1;
                    continue;
                }

                secondAnagram.Add(c, 1);
            }

        foreach (var kvp in fistAnagram) {
            var fistAnagramChar = kvp.Key;
            var firstAnagramCharCount = kvp.Value;

            if (!secondAnagram.ContainsKey(fistAnagramChar)) {
                return false;
            }

            var secondAnagramCharCount = secondAnagram[fistAnagramChar];
            if (firstAnagramCharCount != secondAnagramCharCount) {
                return false;
            }
        }
    
        return true;
    }
}
