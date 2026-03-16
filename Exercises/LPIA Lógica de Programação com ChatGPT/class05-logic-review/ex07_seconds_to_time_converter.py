total_seconds = int(input('Insert the seconds: '))

hours = total_seconds // 3600
rest = total_seconds % 3600
minutes = rest // 60
seconds = rest % 60

print(f'{hours}:{minutes:02d}:{seconds:02d}')