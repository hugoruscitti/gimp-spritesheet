#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *

def integrate(image, drawable, frames):
    new_width = int(image.width / frames)
    image.undo_group_start()
    image.merge_visible_layers(0)
    layers = []

    # Genera un layer por cada cuadro de animacion
    for frame in range(0, int(frames)):
        new_layer = image.layers[0].copy()
        layers.append(new_layer)

    # Elimina los layers anteriores (bah, es uno nomas).
    for layer in image.layers:
        image.remove_layer(layer)

    layers.reverse()

    # inserta las capas alineadas a la misma posicion.
    for (pos, layer) in enumerate(layers):
        image.add_layer(layer)
        delta_x = (pos - (frames-1)) * new_width
        layer.resize(int(new_width), int(image.height), int(delta_x), 0)
        layer.translate(int(delta_x), 0)

    image.resize(new_width, image.height, 0, 0)
    image.undo_group_end()

if __name__ == '__main__':
    register(
            "integrate",
            "Integrate sprites",
            "Integrate sprites",
            "Hugo Ruscitti",
            "Hugo Ruscitti",
            "2010",
            "<Image>/Python-Fu/SpriteTool/Integrate",
            "RGB*, GRAY*",
            [
                (PF_SPINNER, "frames", "Frames", 2, (0, 50, 1)),
            ],
            [],
            integrate)
    main()
