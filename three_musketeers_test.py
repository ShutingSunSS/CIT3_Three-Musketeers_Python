from three_musketeers import *   # import everything from your module
import unittest  # This loads the testing methods and a main program

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual(string_to_location('A1'), (0, 0))
        self.assertEqual(string_to_location('E5'), (4, 4))      
        self.assertEqual(string_to_location('C3'), (2, 2))
       
    def test_location_to_string(self):
        self.assertEqual(location_to_string((0, 0)), 'A1')
        self.assertEqual(location_to_string((4, 4)), 'E5')
        self.assertEqual(location_to_string((2, 2)), 'C3')

    def test_at(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((4, 3)), 'R')
        self.assertEqual(at((2, 2)), 'M')

    def test_all_locations(self):
        self.assertEqual(all_locations(),
                         [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                          (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                          (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                          (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                          (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
    
    def test_adjacent_location(self):
        self.assertEqual(adjacent_location((0, 0), left), (0, -1))
        self.assertEqual(adjacent_location((0, 0), right), (0, 1))
        self.assertEqual(adjacent_location((0, 0), up), (-1, 0))
        self.assertEqual(adjacent_location((0, 0), down), (1, 0))

        self.assertEqual(adjacent_location((2, 2), left), (2, 1))
        self.assertEqual(adjacent_location((2, 2), right), (2, 3))
        self.assertEqual(adjacent_location((2, 2), up), (1, 2))
        self.assertEqual(adjacent_location((2, 2), down), (3, 2))
        
    def test_is_legal_move_by_musketeer(self):
        self.assertEqual(is_legal_move_by_musketeer((2, 2), left), True)
        self.assertEqual(is_legal_move_by_musketeer((2, 2), right), True)
        self.assertEqual(is_legal_move_by_musketeer((2, 2), up), True)
        self.assertEqual(is_legal_move_by_musketeer((2, 2), down), False)

        self.assertEqual(is_legal_move_by_musketeer((0, 3), left), False)
        self.assertEqual(is_legal_move_by_musketeer((0, 3), right), False)
        self.assertEqual(is_legal_move_by_musketeer((0, 3), up), False)
        self.assertEqual(is_legal_move_by_musketeer((0, 3), down), False)

    def test_is_legal_move_by_enemy(self):
        self.assertEqual(is_legal_move_by_enemy((2, 1), left), True)
        self.assertEqual(is_legal_move_by_enemy((2, 1), right), False)
        self.assertEqual(is_legal_move_by_enemy((2, 1), up), True)
        self.assertEqual(is_legal_move_by_enemy((2, 1), down), False)

        self.assertEqual(is_legal_move_by_enemy((4, 3), left), True)
        self.assertEqual(is_legal_move_by_enemy((4, 3), right), True)
        self.assertEqual(is_legal_move_by_enemy((4, 3), up), True)
        self.assertEqual(is_legal_move_by_enemy((4, 3), down), False)

    def test_is_legal_move(self):
        self.assertEqual(is_legal_move((1, 3), left), True)
        self.assertEqual(is_legal_move((0, 1), right), False)
        self.assertEqual(is_legal_move((2, 1), up), True)
        self.assertEqual(is_legal_move((4, 4), down), False)

    def test_has_some_legal_move_somewhere(self):
        set_board([  [_, _, _, M, _],
                     [_, R, _, M, _],
                     [_, _, M, _, R],
                     [_, R, _, _, _],
                     [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))

        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))

        set_board([ [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, M, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ])
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertFalse(has_some_legal_move_somewhere('R'))

    def test_possible_moves_from(self):
        # Nobody
        self.assertEqual(possible_moves_from((0, 0)), [])
        self.assertEqual(possible_moves_from((-5, 3)), [])
        self.assertEqual(possible_moves_from((4, 8)), [])
        # Musketeer
        self.assertEqual(possible_moves_from((0, 3)), [])
        self.assertEqual(possible_moves_from((1, 3)), [down, left])
        self.assertEqual(possible_moves_from((2, 2)), [up, left, right])
        # Enemy
        self.assertEqual(possible_moves_from((1, 2)), [up, left])
        self.assertEqual(possible_moves_from((3, 1)), [down, left, right])
        self.assertEqual(possible_moves_from((4, 3)), [up, left, right])
        

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(can_move_piece_at((0, 0)))
        self.assertFalse(can_move_piece_at((1, 3)))
        self.assertFalse(can_move_piece_at((0, 4)))
        self.assertFalse(can_move_piece_at((4, 0)))
        self.assertFalse(can_move_piece_at((-1, 0)))
        self.assertFalse(can_move_piece_at((5, 8)))
        
        self.assertTrue(can_move_piece_at((0, 3)))
        self.assertTrue(can_move_piece_at((1, 4)))
        self.assertTrue(can_move_piece_at((2, 2)))
        self.assertTrue(can_move_piece_at((2, 2)))

    def test_is_legal_location(self):
        self.assertEqual(is_legal_location((-1, 0)), False)
        self.assertEqual(is_legal_location((0, 0)), True)
        self.assertEqual(is_legal_location((4, 4)), True)
        self.assertEqual(is_legal_location((0, -1)), False)
        self.assertEqual(is_legal_location((5, 3)), False)

    def test_is_within_board(self):
        self.assertEqual(is_within_board((0, 0), left), False)
        self.assertEqual(is_within_board((4, 4), right), False)
        self.assertEqual(is_within_board((0, 4), up), False)
        self.assertEqual(is_within_board((4, 0), down), False)

        self.assertEqual(is_within_board((3, 2), up), True)
        self.assertEqual(is_within_board((2, 3), down), True)

    def test_all_possible_moves_for(self):
        # Order is important for this function, I use: up, down, left, right
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        # Musketeer
        self.assertEqual(all_possible_moves_for('M'), [((0, 3), 'left'), ((0, 3), 'right'), ((1, 4), 'up')])
        # Enemy
        self.assertEqual(all_possible_moves_for('R'), [((0, 2), 'down'), ((0, 2), 'left')])

        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, _, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        # Musketeer
        self.assertEqual(all_possible_moves_for('M'), [((1, 3), 'down'), ((1, 3), 'left'), ((2, 2), 'up'), ((2, 2), 'right')])
        # Enemy
        self.assertEqual(all_possible_moves_for('R'), [((1, 2), 'up'), ((1, 2), 'left'),((2, 3), 'down'), ((2, 3), 'right'), ((3, 1), 'up'), ((3, 1), 'down'), ((3, 1), 'left'), ((3, 1), 'right'), ((4, 3), 'up'), ((4, 3), 'left'),  ((4, 3), 'right')])

    def test_make_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )

        make_move((0, 3), 'right')
        self.assertEqual([ [_, _, R, _, M],
                           [_, _, _, M, M],
                           [_, _, _, _, _],
                           [_, _, _, _, _],
                           [_, _, _, _, _] ],
                         get_board())

        make_move((0, 2), 'down')
        self.assertEqual([ [_, _, _, _, M],
                           [_, _, R, M, M],
                           [_, _, _, _, _],
                           [_, _, _, _, _],
                           [_, _, _, _, _] ],
                         get_board())

        make_move((-1, 0), 'up')
        self.assertEqual([ [_, _, _, _, M],
                           [_, _, R, M, M],
                           [_, _, _, _, _],
                           [_, _, _, _, _],
                           [_, _, _, _, _] ],
                         get_board())

    def test_choose_computer_move(self):
        # should work for both 'M' and 'R'
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, M, _, R],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )

        self.assertEqual(choose_computer_move('R'), ((2, 4), 'left'))
        self.assertEqual(choose_computer_move('M'), ((0, 3), 'left'))
        
    def test_is_enemy_win(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, _, _, R],
                    [M, _, M, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, R, M, R],
                    [_, _, _, _, _],
                    [_, _, M, _, _],
                    [_, M, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, R, M, R],
                    [_, _, _, _, _],
                    [_, _, M, _, _],
                    [_, _, _, _, _],
                    [_, _, _, M, _] ] )
        self.assertFalse(is_enemy_win())


unittest.main()  # outside the class--this tells the framework to run
