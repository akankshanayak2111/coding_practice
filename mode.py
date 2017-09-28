def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    count = {}

    for num in nums:
    	if num not in count:
    		count[num] = 1
    	else:
    		count[num] += 1

    max_v = 0
    mode = set()
   	for k, v in count.items():
   		if v > max_v:
   			max_v = v
   			mode.add(k)
   	return mode


