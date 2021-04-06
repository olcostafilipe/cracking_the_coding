"""
Question 07: Rotate matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""

import numpy as np  # just for visualization

def is_valid(image: list) -> bool:
    return len(image) > 0 and len(image) == len(image[0])


def rotate_image_90(image: list) -> list:
    if not is_valid(image):
        print("Image is not valid!")
        return None

    dim = len(image)
    for layer in range(dim//2):
        first, last = layer, (dim - 1 - layer)
        for i in range(first, last):
            offset = i - first
            top = image[first][i]
            # Rotate left -> top
            image[first][i] = image[last - offset][first]
            # Rotate top -> right
            image[last - offset][first] = image[last][last - offset]
            # Rotate right -> bottom
            image[last][last - offset] = image[i][last]
            # Rotate bottom -> left
            image[i][last] = top

    return image


def main():
    # Matrices do test
    mat_01 = np.array([[1, 1, 1, 1, 1],
                       [2, 2, 2, 2, 2],
                       [3, 3, 3, 3, 3],
                       [4, 4, 4, 4, 4],
                       [5, 5, 5, 5, 5]])

    mat_02 = np.array([[1, 2, 3, 4, 5, 6],
                       [2, 4, 6, 8, 10, 12],
                       [3, 6, 9, 12, 15, 18],
                       [4, 8, 12, 16, 20, 24],
                       [5, 10, 15, 20, 25, 30],
                       [6, 12, 18, 24, 30, 36]])

    mat_03 = np.array([[1, 2, 3, 4],
                       [2, 4, 6, 8],
                       [3, 6, 9, 12],
                       [4, 8, 12, 16],
                       [5, 10, 15, 20]])
    
    mat_04 = np.array([[7, 1, 3, 7, 2],
                       [4, 0, 9, 5, 3],
                       [6, 3, 3, 2, 8],
                       [5, 3, 6, 4, 9],
                       [7, 0, 1, 2, 5]])

    print(mat_01)
    print(rotate_image_90(mat_01))
    print()
    print(mat_02)
    print(rotate_image_90(mat_02))
    print()
    print(mat_03)
    print(rotate_image_90(mat_03))
    print()
    print(mat_04)
    print(rotate_image_90(mat_04))


if __name__ == '__main__':
    main()
