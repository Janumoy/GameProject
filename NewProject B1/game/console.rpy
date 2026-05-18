
default watched_variables = ["RorL", "cold", "warm", "stress", "pills_taken", "insight", "balcony_skipped"]

init python:
    import time

    # Специальный объект для обозначения отсутствующей переменной
    _MISSING = object()
    # Хранилище последних значений и времени изменения:
    # ключ = имя переменной, значение = {"last": предыдущее_значение, "time": время_изменения}
    _watch_state = {}

# Экран-наблюдатель с эффектом смены цвета
screen variable_watcher():
    frame:
        background "#000000cc"
        xalign 0.0 yalign 0.0
        xpadding 10 ypadding 10
        vbox:
            text "Variable Watcher" color "#ffffff" size 20 bold True
            null height 5
            for varname in watched_variables:
                python:
                    now = time.time()
                    # Получаем текущее значение (или метку отсутствия)
                    val = getattr(store, varname, _MISSING)
                    # Состояние отслеживания для этой переменной
                    state = _watch_state.get(varname)
                    if state is None:
                        # Первый показ — запоминаем значение и не подсвечиваем
                        _watch_state[varname] = {"last": val, "time": 0.0}
                    else:
                        # Если значение изменилось, фиксируем время
                        if state["last"] != val:
                            state["last"] = val
                            state["time"] = now
                # Вычисляем, сколько прошло с момента изменения
                $ elapsed = now - _watch_state[varname]["time"]
                # Длительность затухания (в секундах) — можно менять
                $ fade_duration = 2.0
                # Цвет: от красного (#ff0000) к зелёному (#00ff00)
                if elapsed < fade_duration:
                    $ t = elapsed / fade_duration
                    $ color = Color("#ff0000").interpolate(Color("#00ff00"), t)
                else:
                    $ color = "#00ff00"
                # Текст с актуальным значением
                if val is _MISSING:
                    $ display = "<не найдена>"
                else:
                    $ display = val
                text "[varname] = [display]" color color size 16

# Пустой экран-слушатель клавиш (работает во всех контекстах)
screen key_listener():
    key "K_F5" action ToggleScreen("variable_watcher")   # Открыть/закрыть наблюдатель по F5

init python:
    config.overlay_screens.append("key_listener")