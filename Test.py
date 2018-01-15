from Battleship.Battleship import Battleship
from Battleship.Coord import Coord
from Battleship.Direction import Direction
from Battleship.Board import Board


if __name__ == "__main__":
    battleship = Battleship()

    assert (battleship.currentPlayer == 1)

    assert (battleship.placeBoat(0, Coord(4, 2), Direction(Direction.DOWN)))
    assert (battleship.placeBoat(1, Coord(0, 1), Direction(Direction.RIGHT)))
    assert (battleship.placeBoat(2, Coord(3, 8), Direction(Direction.DOWN)))
    assert (battleship.placeBoat(3, Coord(5, 4), Direction(Direction.DOWN)))
    assert (battleship.placeBoat(4, Coord(2, 1), Direction(Direction.RIGHT)))

    battleship.nextPlayer()
    assert (battleship.currentPlayer == 2)

    assert (battleship.placeBoat(0, Coord(0, 0), Direction(Direction.RIGHT)))
    assert (battleship.placeBoat(1, Coord(1, 0), Direction(Direction.RIGHT)))
    assert (battleship.placeBoat(2, Coord(2, 0), Direction(Direction.RIGHT)))
    assert (battleship.placeBoat(3, Coord(3, 0), Direction(Direction.RIGHT)))
    assert (battleship.placeBoat(4, Coord(4, 0), Direction(Direction.RIGHT)))

    battleship.shoot(Coord(0, 2))
    assert (battleship.getCurrentPlayerBoards()[1].board[0, 2] == Board.SHOT_HIT)
    assert (battleship.getOtherPlayerBoards()[0].board[0, 2] == Board.SHOT_HIT)
    assert(battleship.getOtherPlayerBoards()[0].boats[1].squares[Coord(0, 2)] == 1)

    battleship.shoot(Coord(0, 1))
    assert (battleship.getCurrentPlayerBoards()[1].board[0, 1] == Board.SHOT_HIT)
    assert (battleship.getOtherPlayerBoards()[0].board[0, 1] == Board.SHOT_HIT)
    assert (battleship.getOtherPlayerBoards()[0].boats[1].squares[Coord(0, 1)] == 1)

    battleship.shoot(Coord(0, 3))
    assert (battleship.getCurrentPlayerBoards()[1].board[0, 3] == Board.SHOT_SUNK)
    assert (battleship.getOtherPlayerBoards()[0].board[0, 3] == Board.SHOT_SUNK)
    assert (battleship.getOtherPlayerBoards()[0].boats[1].squares[Coord(0, 3)] == 1)
    assert (battleship.getOtherPlayerBoards()[0].boats[1].isDestroyed())

    assert (battleship.getOtherPlayerBoards()[0].board[0, 0] == 0)
    battleship.shoot(Coord(0, 0))
    assert (battleship.getCurrentPlayerBoards()[1].board[0, 0] == Board.SHOT_MISSED)
    assert (battleship.getOtherPlayerBoards()[0].board[0, 0] == Board.SHOT_MISSED)

    battleship.nextPlayer()
    assert (battleship.currentPlayer == 1)

    battleship.shoot(Coord(2, 2))
    assert (battleship.getCurrentPlayerBoards()[1].board[2, 2] == Board.SHOT_HIT)
    assert (battleship.getOtherPlayerBoards()[0].board[2, 2] == Board.SHOT_HIT)

    battleship.shoot(Coord(2, 3))
    assert (battleship.getCurrentPlayerBoards()[1].board[2, 3] == Board.SHOT_MISSED)
    assert (battleship.getOtherPlayerBoards()[0].board[2, 3] == Board.SHOT_MISSED)

    battleship.nextPlayer()
    assert (battleship.currentPlayer == 2)

    for boat in battleship.getOtherPlayerBoards()[0].boats.values():
        for square in boat.squares.keys():
            if boat.squares[square] == 0:
                battleship.shoot(square)
                assert (battleship.getCurrentPlayerBoards()[1].board[square.x, square.y] in [Board.SHOT_HIT, Board.SHOT_SUNK])
                assert (battleship.getOtherPlayerBoards()[0].board[square.x, square.y] in [Board.SHOT_HIT, Board.SHOT_SUNK])
        assert (boat.isDestroyed())

    assert (battleship.winner == 2)


