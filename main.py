def main():
    global color, dead_reds, dead_cyans

    class square:
        def __init__(self, figure):
            self.figure = figure

        def change_figure(self, figure):
            self.figure = figure

    def draw():
        for i in range(50):
            print()

        d_cyans = ' '.join(dead_cyans)
        d_reds = ' '.join(dead_reds)

        print(f'  a b c d e f g h       Dead:')
        print(f'8 {a8.figure} {b8.figure} {c8.figure} {d8.figure} {e8.figure} {f8.figure} {g8.figure} {h8.figure} 8     {d_cyans}')
        print(f'7 {a7.figure} {b7.figure} {c7.figure} {d7.figure} {e7.figure} {f7.figure} {g7.figure} {h7.figure} 7     {d_reds}')
        print(f'6 {a6.figure} {b6.figure} {c6.figure} {d6.figure} {e6.figure} {f6.figure} {g6.figure} {h6.figure} 6')
        print(f'5 {a5.figure} {b5.figure} {c5.figure} {d5.figure} {e5.figure} {f5.figure} {g5.figure} {h5.figure} 5')
        print(f'4 {a4.figure} {b4.figure} {c4.figure} {d4.figure} {e4.figure} {f4.figure} {g4.figure} {h4.figure} 4')
        print(f'3 {a3.figure} {b3.figure} {c3.figure} {d3.figure} {e3.figure} {f3.figure} {g3.figure} {h3.figure} 3')
        print(f'2 {a2.figure} {b2.figure} {c2.figure} {d2.figure} {e2.figure} {f2.figure} {g2.figure} {h2.figure} 2')
        print(f'1 {a1.figure} {b1.figure} {c1.figure} {d1.figure} {e1.figure} {f1.figure} {g1.figure} {h1.figure} 1')
        print(f'  a b c d e f g h  ')

    def move():
        global color
        global dead_reds, dead_cyans

        while True:
            try:
                if color == 'red':
                    move = input(f'Move: ')
                else:
                    move = input(f'Move: ')

                if figurs[move[-2:]].figure.startswith(f''):
                    dead_cyans.append(figurs[move[-2:]].figure)

                    dead_cyans.sort()

                elif figurs[move[-2:]].figure.startswith(f''):
                    dead_reds.append(figurs[move[-2:]].figure)

                    dead_reds.sort()

                figurs[move[-2:]].change_figure(figurs[move[0:2]].figure)
                figurs[move[0:2]].change_figure('·')

                break
            except:
                print('Error')

        if color == 'red': color = 'cyan'
        else: color = 'red' 

    def check_is_queen():
        squares = [a8, b8, c8, d8, e8, f8, g8, h8, a1, b1, c1, d1, e1, f1, g1, h1]

        for square in squares:
            if square.figure == 'p':
                square.figure = 'q'
            elif square.figure == 'P':
                square.figure = 'Q' 
            
    a8, b8, c8, d8, e8, f8, g8, h8 = square('r'), square('n'), square('b'), square('q'), square('k'), square('b'), square('n'), square('r'),
    a7, b7, c7, d7, e7, f7, g7, h7 = square('p'), square('p'), square('p'), square('p'), square('p'), square('p'), square('p'), square('p')
    a6, b6, c6, d6, e6, f6, g6, h6 = square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·')
    a5, b5, c5, d5, e5, f5, g5, h5 = square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·')
    a4, b4, c4, d4, e4, f4, g4, h4 = square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·')
    a3, b3, c3, d3, e3, f3, g3, h3 = square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·'), square('·')
    a2, b2, c2, d2, e2, f2, g2, h2 = square('P'), square('P'), square('P'), square('P'), square('P'), square('P'), square('P'), square('P')
    a1, b1, c1, d1, e1, f1, g1, h1 = square('R'), square('N'), square('B'), square('Q'), square('K'), square('B'), square('N'), square('R')
            
    figurs = {
        'a8': a8, 'b8': b8, 'c8': c8, 'd8': d8, 'e8': e8, 'f8': f8, 'g8': g8, 'h8': h8,
        'a7': a7, 'b7': b7, 'c7': c7, 'd7': d7, 'e7': e7, 'f7': f7, 'g7': g7, 'h7': h7,
        'a6': a6, 'b6': b6, 'c6': c6, 'd6': d6, 'e6': e6, 'f6': f6, 'g6': g6, 'h6': h6,
        'a5': a5, 'b5': b5, 'c5': c5, 'd5': d5, 'e5': e5, 'f5': f5, 'g5': g5, 'h5': h5,
        'a4': a4, 'b4': b4, 'c4': c4, 'd4': d4, 'e4': e4, 'f4': f4, 'g4': g4, 'h4': h4,
        'a3': a3, 'b3': b3, 'c3': c3, 'd3': d3, 'e3': e3, 'f3': f3, 'g3': g3, 'h3': h3,
        'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2,
        'a1': a1, 'b1': b1, 'c1': c1, 'd1': d1, 'e1': e1, 'f1': f1, 'g1': g1, 'h1': h1,
    }

    color = 'cyan'

    dead_reds = []
    dead_cyans = []

    while True:
        draw()
        move()
        check_is_queen()

if __name__ == '__main__':
    main()