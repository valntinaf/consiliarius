VERY_POSITIVE_EMOJIS = "ππππππππ€£ππ₯°ππππππ»"
POSITIVE_EMOJIS = "π€βΊοΈππππππππ€ͺπ§π€ππ₯Έπ€©π₯³ππ€π€π€­π€«π¬π€€π€π€π€ ππΊπΈπΉπΌπ½π"
NEGATIVE_EMOJIS = "π€¨πΏπππππβΉοΈπ£ππ«π©π­π¨π±π°π₯πππ’πͺπ€§π·π€ππΏπΎπ©"
VERY_NEGATIVE_EMOJIS = "π€π π‘π€¬π€―π³π₯΅π₯Άπ€₯"
THE_FACE = "ππ"

EMOJIS_SCORES = {}
EMOJIS_SCORES.update({i: 0.1 for i in VERY_NEGATIVE_EMOJIS})
EMOJIS_SCORES.update({i: 0 for i in THE_FACE})
EMOJIS_SCORES.update({i: 0.3 for i in NEGATIVE_EMOJIS})
EMOJIS_SCORES.update({i: 0.7 for i in POSITIVE_EMOJIS})
EMOJIS_SCORES.update({i: 0.9 for i in VERY_POSITIVE_EMOJIS})

EMOJIS = VERY_POSITIVE_EMOJIS + POSITIVE_EMOJIS + NEGATIVE_EMOJIS + VERY_NEGATIVE_EMOJIS + THE_FACE


def get_score_from_emoji(emoji):
    if score := EMOJIS_SCORES.get(emoji, None):
        return score
    else:
        return 0.5
