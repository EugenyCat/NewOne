# drew carpet

def draw_carpet(w, h):
    w_mid = w / 2
    h_mid = h / 2
    for item_y in range(0, h):
        carpet = ''
        for item_x in range(0, w):
            if item_y % 4 == 0:
                if item_y <= 20 or item_y >= h - 20:
                    if (item_x <= 12 or item_x >= w - 12) and item_x % 2 == 0:
                        carpet += ' '
                    elif (item_x <= 12 or item_x >= w - 12) and item_x % 2 != 0:
                        carpet += '+'
                    elif (item_x >= 12 or item_x <= w - 12) and (item_x % 4 != 0 and item_x % 2 == 0):
                        carpet += '+'
                    else:
                        carpet += ' '
                else:
                    if (item_x <= 12 or item_x >= w - 12):
                        if item_x % 2 == 0:
                            carpet += ' '
                        elif item_x % 2 != 0:
                            carpet += '+'
                    elif (item_x >= 12 or item_x <= w - 12) and (item_x <= 26 or item_x >= w - 26):
                        if (item_x % 4 != 0 and item_x % 2 == 0):
                            carpet += '+'
                        else:
                            carpet += ' '
                    elif (item_x >= 26 or item_x <= w - 26):
                        if (item_x % 2 != 0 and item_x % 2 != 0):
                            carpet += '+'
                        else:
                            carpet += ' '
            elif (item_y == 1 or item_y % 2 != 0):
                if (item_x <= 12 or item_x >= w - 12):
                    carpet += '+'
                else:
                    carpet += ' '
            elif item_y % 2 == 0:
                if item_y <= 20 or item_y >= h - 20:
                    if (item_x <= 12 or item_x >= w - 12) and item_x % 2 != 0:
                        carpet += ' '
                    elif (item_x <= 12 or item_x >= w - 12) and item_x % 2 == 0:
                        carpet += '+'
                    elif (item_x >= 12 or item_x <= w - 12) and (item_x % 4 == 0 and item_x % 2 == 0):
                        carpet += '+'
                    else:
                        carpet += ' '
                else:
                    if item_x <= 12 or item_x >= w - 12:
                        if item_x % 2 != 0:
                            carpet += ' '
                        elif item_x % 2 == 0:
                            carpet += '+'
                    elif (item_x >= 12 or item_x <= w - 12) and (item_x <= 26 or item_x >= w - 26):
                        if item_x % 4 == 0:
                            carpet += '+'
                        elif item_x % 4 != 0:
                            carpet += ' '
                    elif (item_x >= 26 or item_x <= w - 26):
                        if item_x % 2 != 0:
                            carpet += ' '
                        elif item_x % 2 == 0:
                            carpet += '+'
        print(carpet)


draw_carpet(90, 70)