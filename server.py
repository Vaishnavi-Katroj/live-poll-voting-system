import socket

HOST = "127.0.0.1"
PORT = 9999

# Users
users = {
    "Aarav": "123",
    "Diya": "123",
    "Rahul": "123",
    "Sneha": "123",
    "Kiran": "123"
}

votes = {}
duplicate_count = {}
failed_logins = {}

# Stats
total_packets = 0
duplicate_packets = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("🚀 UDP Server Running...\n")

while True:
    data, addr = server_socket.recvfrom(1024)
    total_packets += 1

    msg = data.decode()
    parts = msg.split(":")

    # ---------------- LOGIN ----------------
    if parts[0] == "LOGIN":
        user, pwd = parts[1], parts[2]

        if user in users and users[user] == pwd:
            print(f"[LOGIN SUCCESS] {user}")
            server_socket.sendto("SUCCESS".encode(), addr)
        else:
            failed_logins[user] = failed_logins.get(user, 0) + 1
            print(f"[LOGIN FAILED] {user}")
            server_socket.sendto("FAIL".encode(), addr)

    # ---------------- VOTE ----------------
    elif parts[0] == "VOTE":
        user, vote = parts[1], parts[2].lower()

        # Custom packet log
        print(f"[PACKET RECEIVED] {msg}")

        if user in votes:
            duplicate_count[user] = duplicate_count.get(user, 0) + 1
            duplicate_packets += 1

            print(f"[DUPLICATE] {user} tried again")
            server_socket.sendto("ALREADY_VOTED".encode(), addr)

        else:
            votes[user] = vote
            print(f"[VOTE ACCEPTED] {user} -> {vote.upper()}")
            server_socket.sendto("VOTE_ACCEPTED".encode(), addr)

    # ---------------- STATS ----------------
    loss_percent = (duplicate_packets / total_packets) * 100 if total_packets > 0 else 0

    print("\n📊 --- NETWORK STATS ---")
    print(f"Total Packets: {total_packets}")
    print(f"Duplicate Packets: {duplicate_packets}")
    print(f"Loss % (simulated): {loss_percent:.2f}%")

    count = {"a": 0, "b": 0, "c": 0}
    for v in votes.values():
        if v in count:
            count[v] += 1

    print(f"Votes → A:{count['a']} B:{count['b']} C:{count['c']}")
    print("------------------------\n")