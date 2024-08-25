from aiohttp import web
import asyncio

async def handle(request):
    if request.method == 'POST':
        data = await request.text()
        if data == 'hi':
            return web.Response(text="Hello from Server 1!")
        else:
            return web.Response(text="Unsupported message.")
    return web.Response(status=405, text="Method not allowed.")

app = web.Application()
app.router.add_post('/hello', handle)

def run_server():
    web.run_app(app, port=5000)

if __name__ == "__main__":
    run_server()

