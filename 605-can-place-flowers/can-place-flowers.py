class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res, prv, nxt = 0, 0, 0
        if len(flowerbed) > 1:
            nxt = flowerbed[1]
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and prv == 0 and nxt == 0:
                flowerbed[i] = 1
                res += 1
            prv = flowerbed[i]

            if i < len(flowerbed)-2:
                nxt = flowerbed[i+2]
            else:
                nxt = 0

        return res >= n
            