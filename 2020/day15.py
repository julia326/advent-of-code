def find_most_recent_occurrence_with_cache(elt, pos, cache):
    cached_val = cache[elt] if elt in cache else -1
    cache[elt] = pos
    return cached_val


def puzzle(cutoff=2019):
    nums = [0,8,15,2,12,1,4]
    cache = {}  # most recent occurrences: num -> pos; initialize with input nums
    for i, num in enumerate(nums):
        cache[num] = i
        last_num = num

    for i in range(cutoff - len(nums) + 1):
        if i % 1000000 == 0:
            print(i)
        prev_pos = find_most_recent_occurrence_with_cache(last_num, i+6, cache)  # i+1 - length of starting nums
        cur_num = 0 if prev_pos == -1 else i+6 - prev_pos  # age
        last_num = cur_num

    print(last_num)


def main():
    puzzle(cutoff=29999999)


if __name__ == "__main__":
    main()
