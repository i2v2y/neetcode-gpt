from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        result = []
        for num in numbers:
            result.append(self._greedy_tokenizer(str(num), vocab))
        return result

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        return len(self._greedy_tokenizer(text, vocab))

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        return round(self.count_tokens(text, vocab) / len(text.split()), 4)
    
    def _greedy_tokenizer(self, text:str, vocab: Dict[str, int]):
        tokens = []
        i = 0
        while i < len(text):
            token = text[i]
            for l in range(len(text) - i, 0 , -1):
                substr = text[i : i+l]
                if substr in vocab:
                    token = substr
                    break
            tokens.append(token)
            i += len(token)
        return tokens
            
