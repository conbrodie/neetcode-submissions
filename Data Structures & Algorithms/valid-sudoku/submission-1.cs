public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var subGrids = new Dictionary<string, HashSet<char>>();
        var rows = new Dictionary<int, HashSet<char>>();
        var cols = new Dictionary<int, HashSet<char>>();
        for (int i = 0; i < board.Length; i++) {
            for (int j = 0; j < board[i].Length; j++) {

                // Skip invalid numbers
                if (board[i][j] == '.') continue;

                var compKey = $"{i/3}:{j/3}";

                if (!rows.ContainsKey(i)) {
                    rows.Add(i, new HashSet<char>());
                }

                if (!cols.ContainsKey(j)) {
                    cols.Add(j, new HashSet<char>());
                }

                if (!subGrids.ContainsKey(compKey)) {
                    subGrids.Add(compKey, new HashSet<char>());
                }

                if (!rows[i].Add(board[i][j]) || !cols[j].Add(board[i][j]) || !subGrids[compKey].Add(board[i][j])) {
                    return false;
                }
            }
        }

        return true;
    }
}
