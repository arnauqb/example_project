from example_project.calculator import Calculator

class TestCalculator:
    def test__sum(self):
        calculator = Calculator
        assert calculator.sum(1, 1) == 2