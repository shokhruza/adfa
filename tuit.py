class DoramaRecommender:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: x['score'] >= 8.5 and x['length'] <= 10,
             "recommendation": "1. Aldov o'yini (Liar Game)\n2. G'oyib bo'lgan shahar (Erased)"},
            {"condition": lambda x: x['score'] >= 8.5 and x['length'] > 10 and x['length'] <= 20,
             "recommendation": "1. Yigitlar gullardan yaxshi (Hana Yori Dango)\n2. Nodame Kantabile"},
            {"condition": lambda x: x['score'] >= 8.5 and x['length'] > 20,
             "recommendation": "1. Sevgi ustasi (Shitsuren Chocolatier)\n2. Uzoq ta'til (Long Vacation)"},
            {"condition": lambda x: 7.0 <= x['score'] < 8.5 and x['length'] <= 10,
             "recommendation": "1. Yaxshi tong qo'ng'irog'i (Good Morning Call)\n2. Mening xo'jayinim, mening qahramonim (My Boss My Hero)"},
            {"condition": lambda x: 7.0 <= x['score'] < 8.5 and x['length'] > 10 and x['length'] <= 20,
             "recommendation": "1. Apelsin kunlari (Orange Days)\n2. Gokusen (O'qituvchi)"},
            {"condition": lambda x: 7.0 <= x['score'] < 8.5 and x['length'] > 20,
             "recommendation": "1. Beqaror o'pich (Mischievous Kiss: Love in Tokyo)\n2. Hana Kimi (Haqiqiy yigitcha qiz)"},
            {"condition": lambda x: x['score'] < 7.0,
             "recommendation": "1. Yamato Nadeshiko (Go'zal Uyg'onish)\n2. Mukammal yigit (Absolute Boyfriend)"}
        ]

    def ask_user(self):

        try:
            score = float(input("Qaysi doramaning reytingi kerak (1.0 dan 10.0 gacha): "))
            length = int(input("Qancha epizodli dorama kerak (epizodlar soni): "))
        except ValueError:
            print("Iltimos, to'g'ri raqam kiriting.")
            return None

        return {'score': score, 'length': length}

    def infer(self, user_data):
        if not user_data:
            return "Tavsiya berish uchun to'g'ri ma'lumot kiriting."

        for rule in self.rules:
            if rule['condition'](user_data):
                return f"Sizga tavsiya qilinadi:\n{rule['recommendation']}"

        return "Afsuski, sizning talablaringizga mos keladigan dorama topilmadi."


dorama_recommender = DoramaRecommender()

user_data = dorama_recommender.ask_user()

if user_data:
    recommendation = dorama_recommender.infer(user_data)
    print(recommendation)

