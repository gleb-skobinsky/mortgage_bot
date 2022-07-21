RATE_LICT = ["ставк", "став", "проц", "ежемес", "месяч", "месяц"]
INITIAL_LIST = ["начальн", "взнос", "сумм", "стоим"]

def render_responce(text, only_rate, rate_and_down, down, neither):
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += only_rate
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += rate_and_down
            else:
                responce += down
        if len(responce) == 0:
            responce = neither
        return responce

def get_text_from_label(label, text):
    if label == 0:
        return "Возможно, тебе стоит конкретизировать свой вопрос.\nЯ рассчитан только на информацию об ипотеке в Сбере."
    elif label == 1:
        only_rate = "Ставка на жилье в новостройке от 5,7%."
        rate_and_down = "Первоначальный взнос за жилье в новостройке составит от 20% стоимости."
        down = " Первоначальный взнос составит от 20% стоимости."
        neither = "Ставка на жилье на вторичном рынке от 5,7%. Первоначальный взнос составит от 20% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 2:
        only_rate = "Ставка за жилье на вторичном рынке от 10,5%."
        rate_and_down = "Первоначальный взнос на жилье на вторичном рынке составит от 20% стоимости."
        down = " Первоначальный взнос составит от 20% стоимости."
        neither = "Ставка на жилье на вторичном рынке от 10,5%. Первоначальный взнос составит от 20% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 3:
        only_rate = "Ставка на покупку дома от 10,5%."
        rate_and_down = "Первоначальный взнос за покупку дома составит от 20% стоимости."
        down = " Первоначальный взнос составит от 20% стоимости."
        neither = "Ставка на покупку дома от 10,5%. Первоначальный взнос составит от 20% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 4:
        only_rate = "Ставка на строительство дома от 5,3%."
        rate_and_down = "Первоначальный взнос за строительство дома составит от 25% стоимости."
        down = " Первоначальный взнос составит от 25% стоимости."
        neither = "Ставка на строительство дома от 5,3%. Первоначальный взнос составит от 25% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 5:
        only_rate = "Ставка на покупку земли или дачного дома от 10,8%."
        rate_and_down = "Первоначальный взнос за покупку земли или дачного дома составит от 25% стоимости."
        down = " Первоначальный взнос составит от 25% стоимости."
        neither = "Ставка на покупку земли или дачного дома от 10,8%. Первоначальный взнос составит от 25% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 6:
        only_rate = "Ставка рефинансирования ипотеки от 5,7%."
        rate_and_down = "Первоначального взноса за рефинансирование ипотеки нет."
        down = " Первоначального взноса нет."
        neither = "Ставка рефинансирования ипотеки от 5,7%. Первоначального взноса нет."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 7:
        only_rate = "Ставка на покупку гаража, машиноместа или кладовой от 11%."
        rate_and_down = "Первоначальный взнос за покупку гаража, машиноместа или кладовой составит от 25% стоимости."
        down = " Первоначальный взнос составит от 25% стоимости."
        neither = "Ставка на покупку гаража, машиноместа или кладовой от 11%. Первоначальный взнос составит от 25% стоимости."
        return render_responce(text, only_rate, rate_and_down, down, neither)
    elif label == 8:
        only_rate = "Ставка на наличные под залог недвижимости от 10,8%."
        rate_and_down = "Первоначального взноса за наличные под залог недвижимости нет."
        down = " Первоначального взноса нет."
        neither = "Ставка на наличные под залог недвижимости от 10,8%. Первоначального взноса нет."
        return render_responce(text, only_rate, rate_and_down, down, neither)