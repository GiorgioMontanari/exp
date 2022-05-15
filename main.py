

with open('data.csv') as f:
    for r in f:
        r = r.strip()
        accx, accy, accz, tsince, t = r.split(',')
        accx = abs(float(accx))
        accy = abs(float(accy))
        accz = abs(float(accz))

        m = (accx + accy + accz)/3
        # r = post(f'{base_url}/sensors/sensor1', data={'time': t, 'value': pm10, 'secret': secret})
        print('media accelerazione: ',m, t)
