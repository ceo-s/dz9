from main import Player, create_player, create_desk, players

class TestPytestom:
      
    def test_create_player(self):
        create_player("Egor")
        assert list(players.keys()) == ["Egor"]
        create_player("Roman")
        assert list(players.keys()) == ["Egor", "Roman"]

    def test_name(self):
        egor = Player("Egor", create_desk())
        assert egor.name == "Egor"

    def test_create_desk(self):

        egor = Player("Egor", create_desk())
        vasya = Player("Vasya", create_desk())
        assert len(vasya.desk) == len(egor.desk)

    def test_desk(self):
        egor = Player("Egor", create_desk())
        assert len(egor.desk) == 26
        assert egor.desk[8] == egor.desk[17] == "\n"
