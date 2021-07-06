from nanolib import *



ctx = livectx
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peeraddr = random.choice(get_all_dns_addresses(ctx['peeraddr']))
s.connect((peeraddr, ctx['peerport']))
s.settimeout(2)

msg_handshake = message_handshake_query()
s.send(msg_handshake.serialise())
data = read_socket(s, 136)
recvd_response = message_handshake_response.parse_msg_handshake_response(data)

response = message_handshake_response.create_handshake_response(recvd_response.cookie)
s.send(response.serialise())
data = read_socket(s, 104)
recvd_response2 = message_handshake_response.parse_msg_handshake_response(data)