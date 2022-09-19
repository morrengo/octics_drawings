#each line type returns a triple: (line_start, line_end, text_pos)

def middle_vertical(SQUARE_SIZE):
    return(
        (SQUARE_SIZE[0]/2,0),
        (SQUARE_SIZE[0]/2,SQUARE_SIZE[1]),
        (SQUARE_SIZE[0]/2+3,10)
    )