class Solution:

    lst_mapping = []
    def encode(self, strs: List[str]) -> str:
        self.lst_mapping = [(i,s) for i,s in enumerate(strs)]
        str = "".join(strs)
        return str

    def decode(self, s: str) -> List[str]:
        lst = [self.lst_mapping[i][1] for i in range(len(self.lst_mapping))]
        return lst