def convert_seconds(seconds):
 days = seconds // (24 * 3600)
 seconds %= 24 * 3600
 hours = seconds // 3600
 seconds %= 3600
 minutes = seconds // 60
 seconds %= 60
 return f'{days} days {hours} hours {minutes} minutes {seconds} seconds'

print(convert_seconds(123456))

q = []
for num in range(1, 11):
    if num % 2 == 0:
        q.append(num)
print(*q)