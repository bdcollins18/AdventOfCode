import re

f = open("input.txt")
estimate = int(f.readline())
busses = [int(match) for match in re.split(r"[,x]+", f.readline().strip())]
wait_times = [bus - (estimate % bus) for bus in busses]
best = min(zip(wait_times, busses))
print(best[0] * best[1])