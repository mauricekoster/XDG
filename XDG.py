import sys
import os
import ConfigParser

icon_theme_config = None
icons_dirs_list = None

#icon_theme_base_dir = '/usr/share/icons'
icon_theme_base_dir = os.path.join(os.path.expanduser('~'), '.icons')
icon_theme_name = 'gnome'

def get_icon_filename(name, custom_icon_path=None):
    global icon_theme_config, icons_dirs_list
    if icon_theme_config is None:
        icon_theme_config = ConfigParser.ConfigParser()

        icon_theme_config.read(os.path.join(icon_theme_base_dir, icon_theme_name, 'index.theme'))

        dirs = icon_theme_config.get('Icon Theme', 'Directories')
        icons_dirs_list = dirs.split(',')
        icons_dirs_list.reverse()

    found = False
    for d in icons_dirs_list:
        for ext in ['svg', 'png', 'xpm']:
            fn = os.path.join(icon_theme_base_dir, icon_theme_name, d, "%s.%s" % (name, ext))
            if os.path.exists(fn):
                found = True
                break
        if found:
            break

    if not found:
        # Fallback
        fn = 'icons/%s.svg' % name
        if not os.path.exists(fn):
            fn = 'icons/%s.png' % name

    print("icon '%s': %s" % (name, fn))
    return fn
