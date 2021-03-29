import time
import multiprocessing

T1 = time.perf_counter();

def do_something():
    print("Diam sejenak..... 1 detik")
    time.sleep(1)
    print("selesai berdiam...")

# P1 = multiprocessing.Process(target=do_something)
# P2 = multiprocessing.Process(target=do_something)

# P1.start()
# P2.start()
# P1.join()
# P2.join()

Processes = []
for x in range(10):
    P = multiprocessing.Process(target=do_something)
    P.start()
    Processes.append(P)

for process in Processes:
    process.join()

T2 = time.perf_counter()
print(f"Selesai dalam...{round(T2-T1,2)} detik")