import rel
import websocket


def on_message(ws: websocket.WebSocket, message: str):
    print(message)


def on_error(ws: websocket.WebSocket, error: Exception):
    print(error)


def on_close(ws: websocket.WebSocket, close_status_code: str, close_msg: str):
    print("### closed ###")


def on_open(ws: websocket.WebSocket):
    print("Opened connection")


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://api.gemini.com/v1/marketdata/BTCUSD",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever(dispatcher=rel, reconnect=5)  # type: ignore
    rel.signal(2, rel.abort)  # type: ignore
    rel.dispatch()
