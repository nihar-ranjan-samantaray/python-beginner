from time import sleep
percentage = 0
for i in range(6):
    print(f"Hacking Nasa {percentage}%")
    percentage += 20
    sleep(2)
    print("Nasa Hacked Succesfully" if percentage > 100 else "")
