import  time
initial = time.time()

k = 0
while (k<10):
    print("Loading...")
    time.sleep(0.5)
    time.perf_counter()
    k+=1
print("While loop Ran in: ", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(10):
    print("Loading...")
    time.sleep(0.5)
print("For loop Ran in: ", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

