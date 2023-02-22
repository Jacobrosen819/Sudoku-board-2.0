import random


sudoku_row_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_row_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku_col_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_col_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku_square_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_square_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

spot_1 = 0
spot_2 = 0
spot_3 = 0
spot_4 = 0
spot_5 = 0
spot_6 = 0
spot_7 = 0
spot_8 = 0
spot_9 = 0
spot_10 = 0
spot_11 = 0
spot_12 = 0
spot_13 = 0
spot_14 = 0
spot_15 = 0
spot_16 = 0
spot_17 = 0
spot_18 = 0
spot_19 = 0
spot_20 = 0
spot_21 = 0
spot_22 = 0
spot_23 = 0
spot_24 = 0
spot_25 = 0
spot_26 = 0
spot_27 = 0
spot_28 = 0
spot_29 = 0
spot_30 = 0
spot_31 = 0
spot_32 = 0
spot_33 = 0
spot_34 = 0
spot_35 = 0
spot_36 = 0
spot_37 = 0
spot_38 = 0
spot_39 = 0
spot_40 = 0
spot_41 = 0
spot_42 = 0
spot_43 = 0
spot_44 = 0
spot_45 = 0
spot_46 = 0
spot_47 = 0
spot_48 = 0
spot_49 = 0
spot_50 = 0
spot_51 = 0
spot_52 = 0
spot_53 = 0
spot_54 = 0
spot_55 = 0
spot_56 = 0
spot_57 = 0
spot_58 = 0
spot_59 = 0
spot_60 = 0
spot_61 = 0
spot_62 = 0
spot_63 = 0
spot_64 = 0
spot_65 = 0
spot_66 = 0
spot_67 = 0
spot_68 = 0
spot_69 = 0
spot_70 = 0
spot_71 = 0
spot_72 = 0
spot_73 = 0
spot_74 = 0
spot_75 = 0
spot_76 = 0
spot_77 = 0
spot_78 = 0
spot_79 = 0
spot_80 = 0
spot_81 = 0

for i in range(81):
  if i == 0:
    spot_1 = random.choice(sudoku_row_1)
    sudoku_row_1.remove(spot_1)
    sudoku_col_1.remove(spot_1)
    sudoku_square_1.remove(spot_1)
  elif i == 1:
    spot_2 = random.choice(sudoku_row_2)
    sudoku_row_1.remove(spot_2)
    sudoku_col_2.remove(spot_2)
    sudoku_square_1.remove(spot_2)
  elif i == 2:
    spot_3 = random.choice(sudoku_row_3)
    sudoku_row_1.remove(spot_3)
    sudoku_col_3.remove(spot_3)
    sudoku_square_1.remove(spot_3)

  
sudoku_board_row1 = [[spot_1, spot_2, spot_3] , [spot_4, spot_5, spot_6], [spot_7, spot_8, spot_9]]
sudoku_board_row2 = [[spot_10, spot_11, spot_12], [spot_13, spot_14, spot_15], [spot_16, spot_17, spot_18]]
sudoku_board_row3 = [[spot_19, spot_20, spot_21], [spot_22, spot_23, spot_24], [spot_25, spot_26, spot_27]]
sudoku_board_row4 = [[spot_28, spot_29, spot_30], [spot_31, spot_32, spot_33], [spot_34, spot_35, spot_36]]
sudoku_board_row5 = [[spot_37, spot_38, spot_39], [spot_40, spot_41, spot_42], [spot_43, spot_44, spot_45]]
sudoku_board_row6 = [[spot_46, spot_47, spot_48], [spot_49, spot_50, spot_51], [spot_52, spot_53, spot_54]]
sudoku_board_row7 = [[spot_55, spot_56, spot_57], [spot_58, spot_59, spot_60], [spot_61, spot_62, spot_63]]
sudoku_board_row8 = [[spot_64, spot_65, spot_66], [spot_67, spot_68, spot_69], [spot_70, spot_71, spot_72]]
sudoku_board_row9 = [[spot_73, spot_74, spot_75], [spot_76, spot_77, spot_78], [spot_79, spot_80, spot_81]]


print(sudoku_board_row1)
print(sudoku_board_row2)
print(sudoku_board_row3)
print(sudoku_board_row4)
print(sudoku_board_row5)
print(sudoku_board_row6)
print(sudoku_board_row7)
print(sudoku_board_row8)
print(sudoku_board_row9)