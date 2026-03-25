import psutil, time, subprocess, csv

THRESHOLD = 75
LOG = 'autoscale_log.csv'

def check_and_scale():
    cpu = psutil.cpu_percent(interval=2)
    ram = psutil.virtual_memory().percent
    ts = time.strftime('%H:%M:%S')
    print(f"[{ts}] CPU:{cpu}% RAM:{ram}%")
    
    with open(LOG,'a') as f:
        f.write(f"{ts},{cpu},{ram}\n")
    
    if cpu > THRESHOLD:
        print(f"⚠️ CPU exceeded {THRESHOLD}%! Triggering GCP scale-out...")
        with open('scale_trigger.txt','w') as f:
            f.write(f"SCALE_TRIGGERED at {ts} | CPU:{cpu}%")
        return True
    return False

print("🔍 Monitoring started...")
for i in range(30):
    if check_and_scale():
        break
    time.sleep(1)
print("✅ Monitoring complete!")
