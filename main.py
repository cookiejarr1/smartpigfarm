from fastapi import FastAPI
import random

app = FastAPI()


@app.get('/')
async def root():
    return {'example': 'This is an example', 'data': 0}


@app.get('/random')
async def get_random():
    rn = random.randint(0, 100)
    return {'number': rn, 'limit': 100}


@app.get('/sensors')
async def get_sensors_data():
    return {
        'TempHumid1':
            {'date': '03-02-2023',
             'time': '16:30:49',
             'data':
                {'temperature': 30.60000038, 'humidity': 33}
             },
        'TempHumid2':
            {'date': '03-02-2023',
             'time': '16:30:49',
             'data':
                 {'temperature': 30.39999962, 'humidity': 27}
             },
        'TempHumid3':
            {'date': '03-02-2023',
             'time': '16:30:49',
             'data': {'temperature': 30.60000038, 'humidity': 33}
             },
        'TempHumid4':
            {'date': '03-02-2023',
             'time': '16:30:49',
             'data': {'temperature': 30.39999962, 'humidity': 27}
             },
        'Ammonia1':
            {'date': '03-02-2023',
             'time': '16:30:49',
             'data': {'ammonia': 0.003866305}
             }}
