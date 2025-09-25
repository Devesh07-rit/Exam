def triangle_validator(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Check if three given sides can form a valid triangle.
    
    A valid triangle must satisfy all three conditions:
    1. side_a + side_b > side_c
    2. side_a + side_c > side_b
    3. side_b + side_c > side_a
    
    Parameters
    ----------
    side_a : float
        Length of the first side of the triangle.
    side_b : float
        Length of the second side of the triangle.
    side_c : float
        Length of the third side of the triangle.
    
    Returns
    -------
    bool
        True if the sides form a valid triangle, False otherwise.
    """
    return (side_a + side_b > side_c and
            side_a + side_c > side_b and
            side_b + side_c > side_a)


def main():
    """
    Main function to run the triangle validation program.
    Takes three inputs from the user and checks if they form a valid triangle.
    """
    print("Triangle Validator")
    print("===================")

    try:
        side_a = float(input("Enter length of side A: "))
        side_b = float(input("Enter length of side B: "))
        side_c = float(input("Enter length of side C: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    if triangle_validator(side_a, side_b, side_c):
        print(f"The sides {side_a}, {side_b}, {side_c} form a valid triangle ✅")
    else:
        print(f"The sides {side_a}, {side_b}, {side_c} do NOT form a valid triangle ❌")


if __name__ == "__main__":
    main()
