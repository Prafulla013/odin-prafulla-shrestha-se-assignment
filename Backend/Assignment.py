import json

def token_bucket(max_tokens, refill_rate, req_times):
    log = []
    tokens_left = float(max_tokens)  # bucket starts full
    last_check = req_times[0] if req_times else 0.0  # starting point

    for i, req_time in enumerate(req_times):
        # elapsed time since last request
        elapsed = req_time - last_check if i > 0 else 0.0

        # refill
        tokens_left = min(max_tokens, tokens_left + elapsed * refill_rate)

        allowed = False
        if tokens_left >= 1.0:
            allowed = True
            tokens_left -= 1.0

        log.append({
            "t": req_time,
            "allowed": allowed,
            "tokens_after": round(tokens_left, 6)
        })

        last_check = req_time

    return log


if __name__ == "__main__":
    capacity = float(input("Max tokens in the bucket? "))
    rate = float(input("How many tokens per second to add? "))

    print("Request times (comma separated, e.g. 0.0,0.1,0.2):")
    times = [float(t) for t in input().strip().split(",")]

    output = token_bucket(capacity, rate, times)

    print("\nSimulation Result:")
    print(json.dumps(output, indent=2))
