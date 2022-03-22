from net import receive_file, run_server

ADDR = ('172.30.1.21', 9999)

run_server(ADDR, receive_file)
# 매개변수 : Thread(target=thread_fn, args=(client_socket, addr))