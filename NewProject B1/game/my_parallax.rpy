init python:
    def get_mouse_normalized():
        x, y = renpy.get_mouse_pos()
        norm_x = (x / config.screen_width) - 0.5
        norm_y = (y / config.screen_height) - 0.5
        return norm_x, norm_y

    def make_parallax_func(speed, max_offset):
        # Функция должна принимать 3 аргумента: trans, st, at
        def parallax_transform(trans, st, at):
            nx, ny = get_mouse_normalized()
            xoffset = nx * max_offset * speed
            yoffset = ny * max_offset * speed
            # Применяем смещение к переданному трансформу (trans)
            trans.xoffset = xoffset
            trans.yoffset = yoffset
            # Возвращаем время до следующего обновления (секунды)
            return 0.016
        return parallax_transform

    def parallax_layer(speed, max_offset=100):
        return Transform(function=make_parallax_func(speed, max_offset))