public class Solution {

    // Encoder: ["Hello", "World"] => Encode() => "HelloWorld"
    // Decoder: "HelloWorld" => Decode() => ["Hello", "World"]

    // 1. Capitalisation matters
    // 2. Empty string list return empty string list
    // 3. Any size (small to large) -> Efficiency is important 
    // 4. Expect special characters (/*#$...) (1,2,3...infinite)
    // 5. Input string can be different lengths

    // Solutions:
    // 1. Use a non ASCII char as the delimiter 
        // Problem: Business rules changes we would need to update the decode() method
    // 2. Use the length of each string to signify each word
        // 

    public string Encode(IList<string> strs) {
        // takes a list of strings
        // converts to a string
        var encodedStr = "";
        for (int i = 0; i <= strs.Count - 1; i++) {
            encodedStr += $"{strs[i].Length}#{strs[i]}";
        }

        return encodedStr;
    }

    public List<string> Decode(string s) {
        var decodedStr = new List<string>();
        var p1 = 0;
        for(int i = 0; i <= s.Length - 1; i++) {
            if (s[i] == '#')
            {
                
                var partL = int.Parse(s.Substring(p1, i - p1));
                var part = s.Substring(i + 1, partL);
                decodedStr.Add(part);

                // current index + part length + delimiter = start of the new string to decode
                i = i + partL + 1; 
                p1 = i;

                if (i >= s.Length) continue;
            }
        }

        return decodedStr;
   }
}
