RATE_LICT = ["ставк", "став", "проц", "ежемес", "месяч", "месяц"]
INITIAL_LIST = ["начальн", "взнос", "сумм", "стоим"]

def get_text_from_label(label, text):
    if label == 0:
        return "Возможно, тебе стоит конкретизировать свой вопрос.\nЯ рассчитан только на информацию об ипотеке в Сбере."
    elif label == 1:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на жилье в новостройке от 5,7%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на жилье в новостройке составит от 20% стоимости."
            else:
                responce += " Первоначальный взнос составит от 20% стоимости."
        if len(responce) == 0:
            responce = "Ставка на жилье на вторичном рынке от 5,7%. Первоначальный взнос составит от 20% стоимости."
        return responce
    elif label == 2:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на жилье на вторичном рынке от 10,5%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на жилье на вторичном рынке составит от 20% стоимости."
            else:
                responce += " Первоначальный взнос составит от 20% стоимости."
        if len(responce) == 0:
            responce = "Ставка на жилье на вторичном рынке от 10,5%. Первоначальный взнос составит от 20% стоимости."
        return responce
    elif label == 3:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на покупку дома от 10,5%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на покупку дома составит от 20% стоимости."
            else:
                responce += " Первоначальный взнос составит от 20% стоимости."
        if len(responce) == 0:
            responce = "Ставка на покупку дома от 10,5%. Первоначальный взнос составит от 20% стоимости."
        return responce
    elif label == 4:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на на строительство дома от 5,3%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на на строительство дома составит от 25% стоимости."
            else:
                responce += " Первоначальный взнос составит от 25% стоимости."
        if len(responce) == 0:
            responce = "Ставка на строительство дома от 5,3%. Первоначальный взнос составит от 25% стоимости."
        return responce
    elif label == 5:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на покупку земли или дачного дома от 10,8%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на покупку земли или дачного дома составит от 25% стоимости."
            else:
                responce += " Первоначальный взнос составит от 25% стоимости."
        if len(responce) == 0:
            responce = "Ставка на покупку земли или дачного дома от 10,8%. Первоначальный взнос составит от 25% стоимости."
        return responce
    elif label == 6:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка рефинансирования ипотеки от 5,7%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначального взноса на рефинансирование ипотеки нет."
            else:
                responce += " Первоначального взноса нет."
        if len(responce) == 0:
            responce = "Ставка рефинансирования ипотеки от 5,7%. Первоначального взноса нет."
        return responce
    elif label == 7:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на покупку гаража, машиноместа или кладовой от 11%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначальный взнос на покупку гаража, машиноместа или кладовой составит от 25% стоимости."
            else:
                responce += " Первоначальный взнос составит от 25% стоимости."
        if len(responce) == 0:
            responce = "Ставка на покупку гаража, машиноместа или кладовой от 11%. Первоначальный взнос составит от 25% стоимости."
        return responce
    elif label == 8:
        responce = ""
        if any(root in text.lower() for root in RATE_LICT):
            responce += "Ставка на наличные под залог недвижимости от 10,8%."
        if any(root in text.lower() for root in INITIAL_LIST):
            if len(responce) == 0:
                responce += "Первоначального взноса на наличные под залог недвижимости нет."
            else:
                responce += " Первоначального взноса нет."
        if len(responce) == 0:
            responce = "Ставка на наличные под залог недвижимости от 10,8%. Первоначального взноса нет." 
        return responce