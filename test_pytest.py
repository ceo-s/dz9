from main import Player, create_player, players

class TestPytestom:
      
    def test_create_player(self):
        create_player("Egor")
        assert list(players.keys()) == ["Egor"]
        create_player("Roman")
        assert list(players.keys()) == ["Egor", "Roman"]

    def test_name(self):
        egor = Player("Egor", Player.create_desk())
        assert egor.name == "Egor"

    def test_create_desk(self):

        egor = Player("Egor", Player.create_desk())
        vasya = Player("Vasya", Player.create_desk())
        assert len(vasya.desk) == len(egor.desk)

    def test_desk(self):
        egor = Player("Egor", Player.create_desk())
        assert len(egor.desk) == 26
        assert egor.desk[8] == egor.desk[17] == "\n"

    def test_str_dunder(self):
        andruha = Player("Andruha", Player.create_desk())
        assert str(andruha) == f"Никнейм игрока - {andruha.name}."

    def test_comparison(self):
        andruha = Player("Andruha", Player.create_desk())
        roma = Player("Roma", Player.create_desk())
        assert roma == andruha
        roma.desk.append(12)
        assert roma != andruha