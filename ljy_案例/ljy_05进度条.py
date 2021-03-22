import time


recv_size = 0
total_size = 10241


while recv_size < total_size:
    recv_size +=1024
    if recv_size > total_size:
        recv_size = total_size
    persent = recv_size / total_size
    time.sleep(1)
    res = int(50 * persent) *"#"
    print("\r[%-50s] %d%%" % (res, int(persent*100)), end='')

