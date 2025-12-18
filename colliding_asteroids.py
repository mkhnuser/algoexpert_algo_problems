# NOTE: This is crazy, huh?
def collidingAsteroids(asteroids):
    stack = []

    for a in asteroids:
        if a > 0:
            stack.append(a)
            continue

        # NOTE: a <= 0 at this point.
        while True:
            if not stack:
                stack.append(a)
                break
            elif stack[-1] < 0:
                stack.append(a)
                break

            a_size = abs(a)
            prev = stack.pop()
            prev_size = abs(prev)

            if prev_size == a_size:
                break
            elif prev_size > a_size:
                stack.append(prev)
                break
            else:
                # NOTE: a_size > prev_size.
                continue

    return stack


if __name__ == "__main__":
    print(collidingAsteroids([-3, 5, -8, 6, 7, -4, -7]))
    print(collidingAsteroids([-5, -5]))
    print(collidingAsteroids([5, 5]))
    print(collidingAsteroids([1, 2, 3, -4]))
