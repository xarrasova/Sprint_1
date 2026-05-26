time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time = time_str.split(',')
total_min = 0

for part in time:
    parts = part.split()

    for p in parts:

        if 'h' in p:
            hours = int(p.replace('h', ''))
            total_min += hours*60
        elif 'm' in p:
            min = int(p.replace('m', ''))
            total_min += min
        elif 's' in p:
            sec = int(p.replace('s', ''))
            total_min += sec // 60

print(total_min)