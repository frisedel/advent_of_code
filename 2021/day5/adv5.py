#!/usr/bin/env python3

from typing import List, Tuple

def convert_to_tuples(vent_data: List[str]) -> List[List[Tuple[int, int]]]:
    converted_list: List[List[Tuple[int, int]]] = []
    for line in vent_data:
        splitted = line.split()
        part1 = splitted[0].split(",")
        part2 = splitted[2].split(",")
        int_data: List[Tuple[int, int]] = [(int(part1[0]), int(part1[1])), (int(part2[0]), int(part2[1]))]
        converted_list.append(int_data)
    return converted_list


def separate_directions(vent_data: List[List[Tuple[int, int]]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]]]:
    straight_lines: List[List[Tuple[int, int]]] = []
    diagonal_lines: List[List[Tuple[int, int]]] = []
    for vent_line in vent_data:
        if vent_line[0][0] == vent_line[1][0] or vent_line[0][1] == vent_line[1][1]:
            straight_lines.append(vent_line)
        else:
            diagonal_lines.append(vent_line)
    return straight_lines, diagonal_lines


def split_straight(straight_lines: List[List[Tuple[int, int]]]):
    vertical_lines: List[List[Tuple[int, int]]] = []
    horizontal_lines: List[List[Tuple[int, int]]] = []
    for line in straight_lines:
        if line[0][0] == line[1][0]:
            vertical_lines.append(line)
        else:
            horizontal_lines.append(line)
    return (vertical_lines, horizontal_lines)


def swap_points(points: List[Tuple[int, int]]):
    points[0], points[1] = points[1], points[0]


def sort_stright_lists(vertical: List[List[Tuple[int, int]]], horizontal: List[List[Tuple[int, int]]]):
    for points in vertical:
        if points[0][1] > points[1][1]:
            swap_points(points)
    for points in horizontal:
        if points[0][0] > points[1][0]:
            swap_points(points)


def sort_diagonals(diagonal_lines: List[List[Tuple[int, int]]]):
    for points in diagonal_lines:
        if points[0][0] > points[1][0]:
            swap_points(points)


def split_diagonal(diagonal_lines: List[List[Tuple[int, int]]]):
    out: List[List[Tuple[int, int]]] = []
    x_to_y: List[List[Tuple[int, int]]] = []
    for line in diagonal_lines:
        if line[0][0] < line[1][0] and line [0][1] < line[1][1]:
            out.append(line)
        else:
            x_to_y.append(line)
    return (out, x_to_y)


def create_vent_lists(vent_data_tupels: List[List[Tuple[int, int]]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]]]:
    straight_lines, diagonal_lines = separate_directions(vent_data_tupels)
    vertical, horizontal = split_straight(straight_lines)
    sort_stright_lists(vertical, horizontal)
    sort_diagonals(diagonal_lines)
    out, x_to_y = split_diagonal(diagonal_lines)
    return (vertical, horizontal, out, x_to_y)


def get_matrix_size(vent_data: List[List[Tuple[int, int]]]):
    max_value = 0
    for points in vent_data:
        for point in points:
            point_max = max(point)
            if point_max > max_value:
                max_value = point_max
    return max_value + 1


def mark_straight_lines_in_matrix(vertical_lines: List[List[Tuple[int, int]]], horizontal_lines: List[List[Tuple[int, int]]], vent_map: List[List[int]]):
    for vertical_line in vertical_lines:
        vertical_vent_length = vertical_line[1][1]-vertical_line[0][1] +1
        x_value = vertical_line[0][0]
        y_start = vertical_line[0][1]
        for index in range(vertical_vent_length):
            vent_map[y_start+index][x_value] += 1
    for horizontal_line in horizontal_lines:
        horizontal_vent_length = horizontal_line[1][0]-horizontal_line[0][0] +1
        y_value = horizontal_line[0][1]
        x_start = horizontal_line[0][0]
        for index in range(horizontal_vent_length):
            vent_map[y_value][x_start+index] += 1


def mark_diagonal_lines_in_matrix(out: List[List[Tuple[int, int]]], x_to_y: List[List[Tuple[int, int]]], vent_map: List[List[int]]):
    for line in out:
        line_length = line[1][0]-line[0][0]+1
        out_x_start = line[0][0]
        out_y_start = line[0][1]
        for index in range(line_length):
            vent_map[out_y_start+index][out_x_start+index] += 1
    for line in x_to_y:
        line_length = line[1][0]-line[0][0]+1
        x_start = line[0][0]
        y_start = line[0][1]
        for index in range(line_length):
            vent_map[y_start-index][x_start+index] += 1


def count_dangerous_vents(vent_map: List[List[int]]):
    number_dagerous_points = 0
    for column in vent_map:
        for value in column:
            if value > 1:
                number_dagerous_points += 1
    return number_dagerous_points


def create_matrix(matrix_size: int):
    return [[0 for j in range(matrix_size)] for i in range(matrix_size)]


def adv5_1(vertical: List[List[Tuple[int, int]]], horizontal: List[List[Tuple[int, int]]], vent_map: List[List[int]]):
    mark_straight_lines_in_matrix(vertical, horizontal, vent_map)
    return count_dangerous_vents(vent_map)


def adv5_2(out: List[List[Tuple[int, int]]], x_to_y: List[List[Tuple[int, int]]], vent_map: List[List[int]]):
    mark_diagonal_lines_in_matrix(out, x_to_y, vent_map)
    return count_dangerous_vents(vent_map)

def main():
    vent_data = []
    with open("ventlines.txt") as f:
        vent_data = f.readlines()
    f.close

    vent_data_tupels = convert_to_tuples(vent_data)
    matrix_size = get_matrix_size(vent_data_tupels)
    vent_map = create_matrix(matrix_size)
    vertical, horizontal, out, x_to_y = create_vent_lists(vent_data_tupels)

    print("part 1 - number of dangerous straight vents:", adv5_1(vertical, horizontal, vent_map))
    print("part 2 - number of all dangerous vents:", adv5_2(out, x_to_y, vent_map))

if __name__ == '__main__':
    main()
