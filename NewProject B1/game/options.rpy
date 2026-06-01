## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.

# Аудиофайлы
define audio.door = "audio/sound/door.ogg"
define audio.guel = "audio/music/guel.ogg"
define audio.clock = "audio/sound/clock.ogg"
define audio.bedsheet = "audio/sound/bedsheet.ogg"
define audio.door1 = "audio/sound/door1.ogg"
define audio.kapli = "audio/sound/kapli.ogg"
define audio.chairSpeak = "audio/sound/chairSpeaker.ogg"
define audio.skripchair = "audio/sound/skripchair.ogg"
define audio.ten = "audio/music/#10.ogg"
define audio.whisper = "audio/sound/whisper.ogg"
define audio.pills = "audio/sound/pills.ogg"
define audio.eleven = "audio/music/#7.ogg"
define audio.bormot = "audio/sound/bormot.ogg"
define audio.shelestbumagi = "audio/sound/shelestbumagi.ogg"
define audio.POMEXi = "audio/sound/POMEXi.ogg"
define audio.POMEXi_1 = "audio/sound/POMEXi_1.ogg"
define audio.POMEXi_2 = "audio/sound/POMEXi_2.ogg"


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "0.0.6"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
Разработчик: {a=https://steamcommunity.com/id/Janumoy/}Janumoy{/a}\n
Создано для\n 
дипломной работы. \n
""")

define flash = Fade(1.0, 2.0, 0.0, color="#ffffff")

## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "NewProjectB1"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

define config.sample_sound = "sample-sound.ogg"
define config.sample_voice = "sample-voice.ogg"

## Список возможных тестовых звуков
define test_sounds = ["audio/sound/TestSound/lie.mp3", "audio/sound/TestSound/correct.mp3"]
define test_voice = ["audio/sound/TestVoice/1.ogg"]


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.


init python:
    import random
    ## Создаём список ваших треков
    main_menu_playlist = ["audio/music/mainmenu/MainMenu.ogg", "audio/music/mainmenu/#3.ogg", "audio/music/mainmenu/#20.ogg", "audio/music/mainmenu/#24.ogg"]

    chosen_track = random.choice(main_menu_playlist)
    config.main_menu_music = chosen_track

define config.main_menu_music = chosen_track


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = None
define config.exit_transition = None


## Переход между экранами игрового меню.

define config.intra_transition = None


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = None


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 25


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>.
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "NewProjectB1-1777355116"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:
        

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')


## Для совершения покупок в приложении требуется лицензионный ключ Google Play.
## Его можно найти в консоли разработчика Google Play в разделе "Монетизация" >
## "Настройка монетизации" > "Лицензирование".

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

# define build.itch_project = "renpytom/test-project"
