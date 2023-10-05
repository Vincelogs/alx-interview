#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False

    keys = [0]  # Start with the key to the first box.
    visited = [False] * n  # Initialize a list to keep track of visited boxes.
    visited[0] = True  # Mark the first box as visited.

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                keys.append(key)
                visited[key] = True

    # If all boxes are visited, return True; otherwise, return False.
    return all(visited)
