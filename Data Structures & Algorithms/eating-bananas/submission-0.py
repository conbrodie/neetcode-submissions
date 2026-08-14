class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(math.ceil(pile / k) for pile in piles)
        def is_valid_hours(k):
            return hours_needed(k) <= h
        l, r = 1, max(piles)
        while l < r:
            k_per_hour = (l+r) // 2
            if is_valid_hours(k_per_hour):
                # could be valid, however could also be less k in the array
                r = k_per_hour
            else:
                l = k_per_hour + 1

        return r
