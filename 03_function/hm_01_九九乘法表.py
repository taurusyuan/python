def multiple_table():

    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("%d*%d=%2d" % (row, col, col * row) , end=" ")
            print("%d*%d=%d" % (row, col, col * row), end="\t")
            # \t利用了转义字符\，可以保持垂直方向对齐
            col += 1
        print("")
        row += 1