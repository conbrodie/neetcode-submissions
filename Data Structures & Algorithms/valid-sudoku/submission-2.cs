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

                if ((rows.ContainsKey(i) && rows[i].Contains(board[i][j])) ||
                    (cols.ContainsKey(j) && cols[j].Contains(board[i][j])) ||
                    (subGrids.ContainsKey(compKey) && subGrids[compKey].Contains(board[i][j]))) {
                    return false;
                }

                if (!rows.ContainsKey(i)) rows[i] = new HashSet<char>();
                if (!cols.ContainsKey(j)) cols[j] = new HashSet<char>();
                if (!subGrids.ContainsKey(compKey)) subGrids[compKey] = new HashSet<char>();

                rows[i].Add(board[i][j]);
                cols[j].Add(board[i][j]);
                subGrids[compKey].Add(board[i][j]);
            }
        }

        return true;
    }
}
