class Calculator:
    ans = 0

    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def divide(a, b):
        return a / b

    @classmethod
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod
    def clean_ans(cls):
        cls.ans = 0


