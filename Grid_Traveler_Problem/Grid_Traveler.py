def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


if __name__ == "__main__":
    print(grid_traveler(18, 18))
