import speedtest
import threading
import itertools
import time
import sys

def spinner(task_name, stop_event):
    for c in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{task_name}... {c}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")

def run_with_spinner(task_name, func):
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(task_name, stop_event))
    t.start()
    result = func()
    stop_event.set()
    t.join()
    return result

def Speed_Test():
    print("Initializing SpeedTest...")
    st = speedtest.Speedtest()

    run_with_spinner("Finding best server", st.get_best_server)

    down_speed = run_with_spinner("Testing download speed", st.download)
    down_speed = round(down_speed / 10**6, 2)

    up_speed = run_with_spinner("Testing upload speed", st.upload)
    up_speed = round(up_speed / 10**6, 2)

    ping = st.results.ping

    print("✅ Test completed\n")
    print(f"Download Speed : {down_speed} Mbps")
    print(f"Upload Speed   : {up_speed} Mbps")
    print(f"Ping           : {ping} ms")

Speed_Test()
input("\nPress Enter to exit...")
