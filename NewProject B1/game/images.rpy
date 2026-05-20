
# Фон
image bg black = Transform("images/background/black.jpg", size=(1920, 1080))

#Главное Меню
image bg_far = Transform("images/menu/bg_far.png", size=(1920, 1080))
image bg_mid = Transform("images/menu/bg_mid.png", size=(1920, 1080))
image bg_near = Transform("images/menu/bg_near.png", size=(1920, 1080))


#Концепт

image 1 = Transform("images/con1/1.png", size=(1920, 1080))
image 2 = Transform("images/con1/2.png", size=(1920, 1080))
image 3 = Transform("images/con1/3.png", size=(1920, 1080))
image 4 = Transform("images/con1/4.png", size=(1920, 1080))
image 5 = Transform("images/con1/5.png", size=(1920, 1080))
image 6 = Transform("images/con1/6.png", size=(1920, 1080))
image 7 = Transform("images/con1/7.png", size=(1920, 1080))
image 8 = Transform("images/con1/8.png", size=(1920, 1080))
image 9 = Transform("images/con1/9.png", size=(1920, 1080))
image 10 = Transform("images/con1/10.png", size=(1920, 1080))
image 11 = Transform("images/con1/11.png", size=(1920, 1080))
image 12 = Transform("images/con1/12.png", size=(1920, 1080))
image 13 = Transform("images/con1/13.png", size=(1920, 1080))
image 14 = Transform("images/con1/14.png", size=(1920, 1080))
image 15 = Transform("images/con1/15.png", size=(1920, 1080))
image 16 = Transform("images/con1/16.png", size=(1920, 1080))
image 17 = Transform("images/con1/17.png", size=(1920, 1080))
image 18 = Transform("images/con1/18.png", size=(1920, 1080))
image 19 = Transform("images/con1/19.png", size=(1920, 1080))
image 20 = Transform("images/con1/20.png", size=(1920, 1080))
image 21 = Transform("images/con1/21.png", size=(1920, 1080))
image 22 = Transform("images/con1/22.png", size=(1920, 1080))
image 23 = Transform("images/con1/23.png", size=(1920, 1080))
image 24 = Transform("images/con1/24.png", size=(1920, 1080))
image 25 = Transform("images/con1/25.png", size=(1920, 1080))


#МиниАрт
image mini_1 = ("images/mila/miniart/1.png")

#Анимации для главного меню



#Начать
image anim_start_frames:
    Animation(
        "images/menu/animation/load/load1.png", 0.15,
        loop=False
    )

#Загрузить
image anim_load_frames:
    Animation(
        "images/menu/animation/load/load1.png", 0.15,
        "images/menu/animation/load/load2.png", 0.15,
        "images/menu/animation/load/load3.png", 0.15,
        "images/menu/animation/load/load4.png", 0.15,
        loop=False
    )
    
#Настройки
image anim_settings_frames:
    Animation(
        "images/menu/animation/preferences/settings1.png", 0.15,
        "images/menu/animation/preferences/settings2.png", 0.15,
        "images/menu/animation/preferences/settings3.png", 0.15,
        "images/menu/animation/preferences/settings4.png", 0.15,
        loop=False
    )

#Об игре
image anim_about_frames:
    Animation(
        "images/menu/animation/about/about1.png", 0.15,
        "images/menu/animation/about/about2.png", 0.15,
        "images/menu/animation/about/about3.png", 0.15,
        "images/menu/animation/about/about4.png", 0.15,
        loop=False
    )

#Помощь
image anim_help_frames:
    Animation(
        "images/menu/animation/help/help1.png", 0.15,
        "images/menu/animation/help/help2.png", 0.15,
        "images/menu/animation/help/help3.png", 0.15,
        "images/menu/animation/help/help4.png", 0.15,
        loop=False
    )

#Вернуться
image anim_back_frames:
    Animation(
        "images/menu/animation/return/back1.png", 0.10,
        "images/menu/animation/return/back2.png", 0.10,
        "images/menu/animation/return/back3.png", 0.10,
        "images/menu/animation/return/back4.png", 0.10,
        "images/menu/animation/return/back5.png", 0.10,
        "images/menu/animation/return/back6.png", 0.10,
        "images/menu/animation/return/back7.png", 0.10,
        "images/menu/animation/return/back8.png", 0.10,
        loop=False
    )






