from random import choice, randrange
from accounts.models import CustomUser
from prediction.models import Prediction, PredictionCategory

TITLE = {
    'Купівля': [
        'машини', 'коня', 'хати',
        'кролика', 'лому', 'гармоніки',
        'підприємства', 'мотоцикла', 'скейтборда',
        'дому'
    ],
    'Продаж': [
        'автомобіля', 'мобільного телефону',
        'книги', 'ноутбука', 'коня',
        'корови', 'хати', 'одягу',
        'пк', 'товарів для дому'
    ],
    'Послуги': [
        'ремонту', 'консультації', 'прибирання',
        'тренування', 'перевезення', 'уроків',
        'фотосесії', 'вигулу собак',
        'програміста', 'дизайну інтер’єру'
    ]
}


def creation_prediction():
    user = CustomUser.objects.get(pk=1)
    for p in range(25):
        description = '----TEST----'
        price = randrange(500, 1000, 50)
        location = choice(['Львів', 'Київ', 'Топорів', 'Золочів'])
        category_title = choice(['Купівля', 'Продаж', 'Послуги'])
        category, created = PredictionCategory.objects.get_or_create(title=category_title)
        title = f"{category_title} {choice(TITLE[category_title])}"

        prediction = Prediction.objects.create(
            user=user,
            title=title,
            description=description,
            location=location,
            price=price,
            category=category
        )
