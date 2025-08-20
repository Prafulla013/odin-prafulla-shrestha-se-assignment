# odin-prafulla-shrestha-se-assignment

# Backend

# Token Bucket Rate Limiter Simulation

This is a simple Python script to simulate a token bucket algorithm. It's a common way to handle rate limiting in APIs. The script takes a list of request timestamps and simulates whether each request would be allowed or denied.

### What It Does

The script calculates how many tokens are in the bucket at the time of each request, accounting for a refill rate between requests.

- **Capacity:** The max number of tokens the bucket can hold.
- **Refill Rate:** How many tokens are added per second.
- **Requests:** A list of timestamps for each incoming request.

The output shows you, for each request, if it was **allowed** and the number of **tokens remaining**.

### How to Run

1.  Clone this repository to your local machine.
    git clone https://github.com/your-username/token-bucket-simulator.git
2.  Navigate to the project directory.
    cd odin-prafulla-shrestha-se-assignment/backend
3.  Run the script using Python.
    python Assignment.py
4.  The script will prompt you to enter the capacity, refill rate, and a comma-separated list of request timestamps.

### Assumptions / Trade-offs

- **Requests are given as timestamps in seconds** (floats or integers).
- **Refill is linear over time**.
- **No concurrency**: requests are processed sequentially in the given order.
- **Simulation only**: not integrated with a real API server.
- **Tokens cannot exceed capacity**: extra refill tokens are discarded.

---

### Edge Cases Covered

- **Capacity = 0** : No requests can ever be allowed. 
- **Refill Rate = 0** : Bucket never refills, only initial capacity is used. 
- **Multiple requests at the same timestamp** : Processed in sequence, tokens decrease accordingly. 
- **Large time gaps between requests** : Bucket refills up to its maximum capacity.
- **Excessive requests** : Once tokens are depleted, further requests are denied until refill occurs.



### Example

Here's a quick example of the kind of input and output you can expect:

**Input:**
- **Capacity:** 5
- **Refill Rate:** 2
- **Requests:** 0.0, 0.1, 0.2, 1.5, 1.6

**Output:**
The script will print a JSON output showing the status of each request.


json
[
  {
    "t": 0.0,
    "allowed": true,
    "tokens_after": 4.0
  },
  {
    "t": 0.1,
    "allowed": true,
    "tokens_after": 3.2
  },
  {
    "t": 0.2,
    "allowed": true,
    "tokens_after": 2.4
  },
  {
    "t": 1.5,
    "allowed": true,
    "tokens_after": 4.0
  },
  {
    "t": 1.6,
    "allowed": true,
    "tokens_after": 3.2
  }
]

# Frontend

# Chat Grouper
============

A React component that renders a chat timeline with smart grouping and dividers. It handles sorted or unsorted input, inserts day separators, and shows an “Unread” divider based on a read timestamp.

### Setup & run instructions
------------------------

1. Create the app (or open your existing React app)
npx create-react-app chat-grouper
cd chat-grouper

2. Start the dev server

npm start


3. Open the app in your browser

http://localhost:3000

## Assumptions / Trade-offs

- Messages may be **unsorted**; the component always sorts by `createdAt` (then `id` if tied).  
- Consecutive messages by the **same author within 2 minutes** are grouped.  
- **Day separators** are inserted on date changes.  
- **Unread divider** appears once, before the first message after `readAt`.  
- **Current user messages** are rendered differently (right-aligned).  
- **Minimal styling**; focus is on logic correctness.  

---

## Edge Cases Covered

- **Unsorted messages** : correctly sorted.  
- **Same timestamp** : tie-breaker via `id`.  
- **Day changes** : correct day separator and reset grouping.  
- **Unread divider** : only appears once, correctly placed.  
- **Author/group changes** : new bubble started.  
- **Single message / empty array** : renders without errors.  



