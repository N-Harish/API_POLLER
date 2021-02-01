import requests
import time
import asyncio
from MSQ.receiver import receiver
from MSQ.sender import send
from db import get_db_api1, get_db_api2


async def main():
    result = loop.run_in_executor(None, requests.get, 'https://www.thecocktaildb.com/api/json/v1/1/random.php')
    result1 = loop.run_in_executor(None, requests.get, 'https://randomuser.me/api/')
    await asyncio.wait([result, result1])
    return result, result1


if __name__ == '__main__':
    # while True:
    try:
        # Get an event loop
        loop = asyncio.get_event_loop()

        t = time.time()

        # Run main function until code is completed
        res, res1 = loop.run_until_complete(main())

        send(body=res.result().text)
        api1 = get_db_api1()
        receiver(collection=api1)

        send(body=res1.result().text)
        api2 = get_db_api2()
        receiver(collection=api2)

        print(f'total time {time.time() - t}')

    except Exception as e:
        print(e)

    # Restart code after 5 sec
    time.sleep(5)
