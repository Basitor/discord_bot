class Messages:

    @staticmethod
    def help_message() -> str:
        return "Я бот, на данный момент могу потролить юзера 5 раз, если сказать мне:\n" \
                "```@bla_bla_bot разберись за меня с {user}```" \
                "Либо могу прекратить, если инициатор скажет:" \
                "```@bla_bla_bot харош с него```"

    @staticmethod
    def now_trolling(user: str, author: str) -> str:
        return f"{user}, " \
               f"ты надоел {author} " \
               f"и теперь я твой опонент по спорам"

    @staticmethod
    def cant_find_user(user: str) -> str:
        return f"Не могу найти пользователя {user}"

    @staticmethod
    def wrong_troll_name_format() -> str:
        return f"Нахрена ты '@' в запросе написал?? По-русски же написано, что просто ник"

    @staticmethod
    def trolling_already(user: str, author: str) -> str:
        return f"Пагади, уже {user} тролю. " \
               f"Можешь попросить {author} прекратить"

    @staticmethod
    def enough_for_you(user: str) -> str:
        return f"{user} Лан, харош с тебя на этот раз."

    @staticmethod
    def troll_message(user: str) -> str:
        return f"{user} Ты дурак, а?! Писать такие глупости"

    @staticmethod
    def are_author_satisfied(author: str) -> str:
        return f"{author}, надеюсь ты доволен?"
