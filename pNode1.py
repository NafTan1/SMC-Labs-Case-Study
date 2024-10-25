
import asyncio

class PeerNode:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.instructions = []
        self.connections = []

    async def handle_client(self, reader, writer):
        while True:
            data = await reader.read(100)
            if not data:
                break  # Exit if no data is received
            message = data.decode()
            print(f"Node 1 received: {message}")

            response = f"Node 1 processed: {message}"
            writer.write(response.encode())
            await writer.drain()

        writer.close()

    async def run_server(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        print(f'Serving on {self.host}:{self.port}')

        async with server:
            await server.serve_forever()

    async def read_instructions(self, file_path):
        with open(file_path, 'r') as file:
            instructions = file.read().strip().split()
        self.instructions = [instr for instr in instructions if instr.startswith('a')]
        return self.instructions

    async def connect_to_nodes(self, nodes):
        for node_address in nodes:
            try:
                reader, writer = await asyncio.open_connection(*node_address)
                self.connections.append((reader, writer))
                print(f"Node 1 connected to {node_address}")
            except Exception as e:
                print(f"Failed to connect to {node_address}: {e}")

    async def send_instructions(self):
        for instruction in self.instructions:
            print(f"Node 1 sending {instruction}")
            for reader, writer in self.connections:
                writer.write(instruction.encode())
                await writer.drain()
                response = await reader.read(100)
                print(f"Node 1 received: {response.decode()}")

    async def main(self):
        server_task = asyncio.create_task(self.run_server())

        await asyncio.sleep(5)  # Allow time for the server to start

        instructions = await self.read_instructions("instructions.txt")
        print(f"Node 1 instructions: {instructions}")

        # Connect to Node 2
        await self.connect_to_nodes([('localhost', 8889)]) 

        # Send instructions to the connected node(s)
        await self.send_instructions()

        print("Node 1 finished sending instructions. Terminating.")

        for reader, writer in self.connections:
            writer.close()
            await writer.wait_closed()

if __name__ == '__main__':
    node = PeerNode(port=8888)
    asyncio.run(node.main())
