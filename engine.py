
def analyze_orderflow(orderbook):
    bid_volume = sum([x["size"] for x in orderbook["bids"]])
    ask_volume = sum([x["size"] for x in orderbook["asks"]])

    delta = bid_volume - ask_volume

    if delta > 0:
        control = "Buyers in control"
    elif delta < 0:
        control = "Sellers in control"
    else:
        control = "Neutral"

    largest_bid = max(orderbook["bids"], key=lambda x: x["size"])
    largest_ask = max(orderbook["asks"], key=lambda x: x["size"])

    return {
        "bid_volume": bid_volume,
        "ask_volume": ask_volume,
        "delta": delta,
        "control": control,
        "largest_bid": largest_bid,
        "largest_ask": largest_ask
    }
