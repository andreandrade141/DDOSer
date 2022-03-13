import requests


def reqController(url):
    counter = 0
    while counter <= 100000:
        try:
            r = requester(url)
        except:
            pass
        counter += 1


async def requester(url):
    s = requests.get(url)
    print("done")
    return s
