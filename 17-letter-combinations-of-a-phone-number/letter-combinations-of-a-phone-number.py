class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # mapping digits to letters like phone keypad
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        # helper function for backtracking
        def build(index: int, current: list[str]):
            # if we've used all digits → form a word and store it
            if index == len(digits):
                result.append("".join(current))
                return

            # try every possible letter for the current digit
            for letter in mapping[digits[index]]:
                current.append(letter)          # choose a letter
                build(index + 1, current)       # go to next digit
                current.pop()                   # undo choice (backtrack)

        # start from first digit with empty path
        build(0, [])
        return result
        