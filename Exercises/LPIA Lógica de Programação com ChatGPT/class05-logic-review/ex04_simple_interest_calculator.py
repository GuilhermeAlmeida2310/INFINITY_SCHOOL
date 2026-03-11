initial_capital = float(input('Insert the value of initial capital: '))
interest_rate = float(input('Insert the value of interest rate: '))
application_time = int(input('Insert the aplication time: '))

if initial_capital <= 0 or interest_rate <= 0 or application_time <= 0:
    print('Every values need be positives!')
else:
    fees = initial_capital * (interest_rate / 100) * application_time
    final_value = initial_capital + fees

    print(f'Initial Capital: ${initial_capital:.2f}')
    print(f'Interest Rate: {interest_rate:.1f}% to month')
    print(f'Application Time: {application_time} months')
    print(f'Accrued Interest: ${fees:.2f}')
    print(f'Final Value: ${final_value:.2f}')

    month = 1
    while month <= application_time:
        month_interest = initial_capital * (interest_rate / 100) * month
        month_value = initial_capital + month_interest
        print(f'Month: {month}: ${month_value:.2f}')
        month += 1