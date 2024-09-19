"""
You are given an array of non-negative integers where each element represents the
maximum number of steps you can advance in the array. Your goal is to determine
whether it’s possible to advance from the first element to the last.
"""


def array_advance(move_list: list[int]) -> bool:
    furthest_idx = 0
    len_list = len(move_list)

    for idx in range(len_list):
        if idx > furthest_idx:
            return False

        furthest_idx = max(furthest_idx, idx + move_list[idx])

        if furthest_idx > len_list - 1:
            return True

    return True


winnable_game_list = [1, 3, 1, 0, 2, 0, 1]
print(f"{array_advance(winnable_game_list)=}")

unwinnable_game_list = [3, 2, 0, 0, 2, 0, 1]
print(f"{array_advance(unwinnable_game_list)=}")
