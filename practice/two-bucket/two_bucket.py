import copy

def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize the buckets
    buckets = []
    buckets.append({"max": bucket_one, "cur": 0})
    buckets.append({"max": bucket_two, "cur": 0})
    
    # Fill the specified start bucket
    fill(buckets, 0 if start_bucket == "one" else 1)
    
    # Check if the goal is already achieved
    result = is_done(buckets, goal)
    if result:
        return (1, *result)

    # List to store all possible moves
    moves = []
    for i in range(6):
        # Try each move and store the result
        _r = move(i, buckets, goal, start_bucket, 1, [buckets])
        if _r:
            moves.append(_r)
    
    # Return the minimum move required to reach the goal
    return min(moves)

# Function to check if the goal is achieved
def is_done(buckets, goal):
    if buckets[0]["cur"] == goal:
        return ("one", buckets[1]["cur"])
    if buckets[1]["cur"] == goal:
        return ("two", buckets[0]["cur"])
    return False

# Function to perform a move
def move(index, buckets, goal, start_bucket, count, history):
    _buckets = copy.deepcopy(buckets)
    
    # Perform the move based on the index
    if index == 0:
        pour(_buckets, 0, 1)  # Pour from bucket one to bucket two
    elif index == 1:
        pour(_buckets, 1, 0)  # Pour from bucket two to bucket one
    elif index == 2:
        empty(_buckets, 0)     # Empty bucket one
    elif index == 3:
        empty(_buckets, 1)     # Empty bucket two
    elif index == 4:
        fill(_buckets, 0)      # Fill bucket one
    elif index == 5:
        fill(_buckets, 1)      # Fill bucket two

    # Check if both buckets are empty
    if _buckets[0]["cur"] + _buckets[1]["cur"] == 0:
        return False
    
    # Determine which bucket is first and second based on the start bucket
    first_bucket = 0 if start_bucket == "one" else 1
    second_bucket = 1 if start_bucket == "one" else 0
    
    # Check if the move results in an invalid state or if it's already been visited
    if is_empty(_buckets, first_bucket) and is_full(_buckets, second_bucket):
        return False
    if _buckets in history:
        return False
    
    # Check if the goal is achieved after the move
    result = is_done(_buckets, goal)
    if result:
        return (count+1, *result)

    # List to store all possible subsequent moves
    moves = []
    for i in range(6):
        if i == index:
            continue
        _r = move(i, _buckets, goal, start_bucket, count+1, [*history, _buckets])
        if _r:
            moves.append(_r)
    
    # Return the minimum move required to reach the goal
    if moves:
        return min(moves)

# Function to check if a bucket is empty
def is_empty(buckets, which_bucket):
    if buckets[which_bucket]["cur"] == 0:
        return True
    return False

# Function to check if a bucket is full
def is_full(buckets, which_bucket):
    if buckets[which_bucket]["cur"] == buckets[which_bucket]["max"]:
        return True
    return False

# Function to pour water from one bucket to another
def pour(buckets, from_bucket, to_bucket):
    left = buckets[to_bucket]["max"] - buckets[to_bucket]["cur"]
    if buckets[from_bucket]["cur"] > left:
        fill(buckets, to_bucket)
        buckets[from_bucket]["cur"] -= left
    else:
        buckets[to_bucket]["cur"] += buckets[from_bucket]["cur"]
        empty(buckets, from_bucket)

# Function to empty a bucket
def empty(buckets, which_bucket):
    buckets[which_bucket]["cur"] = 0

# Function to fill a bucket
def fill(buckets, which_bucket):
    buckets[which_bucket]["cur"] = buckets[which_bucket]["max"]
