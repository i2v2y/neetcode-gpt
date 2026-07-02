from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        tokens = list(corpus)
        merges = []

        for _ in range(num_merges):
            counts = Counter((tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1))
            pairs = [p for p, c in counts.items() if c == max(counts.values())]
            pair = min(pairs)
            merges.append(pair)
            
            merged = []
            i = 0
            while i < len(tokens):
                if (i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair):
                    merged.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    merged.append(tokens[i])
                    i += 1
            tokens = merged

        return merges
