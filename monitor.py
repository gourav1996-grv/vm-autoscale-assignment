import psutil,time,csv
with open('metrics.csv','w',newline='') as f:
 w=csv.writer(f)
 w.writerow(['time','cpu','ram'])
 for i in range(10):
  w.writerow([time.strftime('%H:%M:%S'),psutil.cpu_percent(1),psutil.virtual_memory().percent])
  print(f"CPU:{psutil.cpu_percent()}% RAM:{psutil.virtual_memory().percent}%")
print("✅ Done!")
