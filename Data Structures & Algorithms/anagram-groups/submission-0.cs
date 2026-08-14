

public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // Dict<int: anagram, List<string>: anagram>  = x, [""], ab, [""], cat, ["act","cat","hat"] ... etc
        var groupedAnagrams = new Dictionary<string, List<string>>();

        // if strs.length == 0 return [[""]]
        if (strs.Length == 0) {
            return new List<List<string>>();
        }

        //  ["act","pots","tops","cat","stop","hat"]
        // act: [""], pots: [""]
        
        foreach (var str in strs) {
            var anagramFound = false;
            foreach (var group in groupedAnagrams) {
                if (group.Key.Length == str.Length) {
                    if (IsAnagram(str, group.Key)) {
                        groupedAnagrams[group.Key].Add(str);
                        anagramFound = true;
                        break;
                    }
                }
            }
            if (!anagramFound) groupedAnagrams.Add(str, new List<string>() { str });
        }

        return groupedAnagrams.Values.ToList();  
    }

    private bool IsAnagram(string value1, string value2) {
        int[] count = new int[26];
        for (int i = 0; i < value1.Length; i++) {
            count[value1[i] - 'a']++;
            count[value2[i] - 'a']--;
        }

        foreach (int val in count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
