import datetime
from View.FirstMenu import menu

print('Hello World!')
print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print('__name__ value: ', __name__)


def main():
    menu()


if __name__ == '__main__':
    main()
    # print(__name__)
