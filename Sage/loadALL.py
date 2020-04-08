import os
for element in os.listdir('.'):
    if sage.repl.load.is_loadable_filename(element):
        load(element)
