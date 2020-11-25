cars, laps = (int(x) for x in input().split())
times      = [sum(int(x) for x in input().split()) for _ in range(cars)]
srtd_times = sorted(times)

print(times.index(srtd_times[0]) + 1)
print(times.index(srtd_times[1]) + 1)
print(times.index(srtd_times[2]) + 1)