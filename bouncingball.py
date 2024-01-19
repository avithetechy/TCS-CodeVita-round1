def calculate_next_position(current_position, direction):
    return [current_position[0] + direction[0], current_position[1] + direction[1]]

def will_balls_overlap(position1, direction1, position2, direction2):
    for _ in range(1000):  # To prevent an infinite loop
        position1 = calculate_next_position(position1, direction1)
        position2 = calculate_next_position(position2, direction2)
        if position1 == position2:
            return True
    return False

def find_min_steps_to_overlap(rows, columns, ball1_position, ball1_direction, ball2_position, ball2_direction):
    for steps in range(1, rows * columns + 1):
        ball1_position = calculate_next_position(ball1_position, ball1_direction)
        ball2_position = calculate_next_position(ball2_position, ball2_direction)
        if ball1_position == ball2_position:
            return steps
    return "Never"

# Input
M, N = map(int, input().split())
ball1_position = list(map(int, input().split()))
ball1_direction = list(map(int, input().split()))
ball2_position = list(map(int, input().split()))
ball2_direction = list(map(int, input().split()))

# Output
result = find_min_steps_to_overlap(M, N, ball1_position, ball1_direction, ball2_position, ball2_direction)
print(result)