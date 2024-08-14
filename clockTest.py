import time
from datetime import timedelta

def main():
    a = 100.0
    b = 120.0
    print(a+b)

start_time = time.monotonic()
main()
end_time = time.monotonic()

print("--- %s seconds ---" % timedelta(seconds=end_time - start_time))