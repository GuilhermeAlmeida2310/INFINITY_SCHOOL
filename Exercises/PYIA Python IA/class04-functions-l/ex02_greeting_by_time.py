def greeting_time(hour):
    if 5 <= hour < 12:
        print('Good Morning!')
    elif 12 <= hour < 18:
        print('Good Afternoon!')
    else:
        print('Good Night!')

greeting_time(8)