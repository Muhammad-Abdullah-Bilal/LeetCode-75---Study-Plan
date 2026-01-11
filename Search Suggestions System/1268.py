class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            start = bisect_left(products, prefix)
            suggestions = []

            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])

            result.append(suggestions)

        return result