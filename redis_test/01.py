
from redis import StrictRedis


def main():
    try:

        sr = StrictRedis()
        res = sr.set('name', 'best')
        print(res)
        num = sr.get('name')
        print(num)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
