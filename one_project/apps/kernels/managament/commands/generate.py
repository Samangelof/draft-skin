from django.core.management.base import BaseCommand
# from kernels.models import GenresMovies, AllFilms, AllSerials
from kernels.models import Warrior, Category


warrior_rank = [
    'Ландмейстер',
    'Император',
    'Король',
    'Князь',
    'Лорд',
    'Даймё',
    'Сёгун',
    'Конунг',

    'Ландскнехт',
    'Рыцарь',
    'Крылатый гусар',
    'Самурай',
    'Ронин',
    'Рейтар',
    'Раубриттер',
    'Батыр',
    'Лучник',
    'Тяжелая кавалерия',
    'Варяг',
    'Берсерк',
    'Викинг',
    'Ветеран',
    'Дружинник',
]

film_name = [
    'Американский пирог свадьба',
    'Мстители',
    'Железный человек',
    'Халк',
    'Черная пантера'
]

film_photo = [
    # 'resource/20220930_134411.jpg',
]

film_rang = [
    2.0,
    1.6,
    9.9,
    7.7,
    6.3
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('sheesh')
    #MAIN                               #MAIN
        # Warrior.objects.all().delete()
        for i in warrior_rank:
            genres = Warrior()
            genres.name = i
            genres.save()

        print('[SUCCESS] Warriors added')
    #MAIN                               #MAIN
    
    #add category                       #add category
        # all_categories = Category.objects.all()
        # for i in all_categories:
        #     genres = Warrior()
        #     genres.category = i
        #     genres.save()
        # print('[SUCCESS] Categories for warriors added')
    #add category                       #add category


    # def repeat(self, choice_list:list):
    #     for q in choice_list:
            
            # name_model = Warrior()._meta.get_fields()[1]
            # model = Warrior()
            # model.name_model = q
            # model.save()



# from kernels.managament.commands.generate import Command
# z = Command()
# z.handle()