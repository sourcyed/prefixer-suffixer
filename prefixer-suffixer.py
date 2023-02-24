import sys
import os

def main(particle, filepath, suffix, additive):
    for root, dirs, files in os.walk(filepath):
        for file in files:
            name, extension = os.path.splitext(file)
            if not additive:
                if not suffix:
                    if name.startswith(particle):
                        new_name = name[name.find(particle) + len(particle):].lstrip() + extension
                        os.rename(os.path.join(root, file), os.path.join(root, new_name))
                else:
                    if name.endswith(particle):
                        new_name = name[:name.find(particle)].rstrip() + extension
                        os.rename(os.path.join(root, file), os.path.join(root, new_name))
            else:
                if not suffix:
                    new_name = particle + name + extension
                else:
                    new_name = name + particle + extension
                os.rename(os.path.join(root, file), os.path.join(root, new_name))



if __name__ == "__main__":
    filepath = "."
    suffix = False
    additive = False

    if len(sys.argv) > 1:
        particle = sys.argv[1]
        if len(sys.argv) > 2:
            filepath = sys.argv[2]
            if not os.path.isdir(filepath):
                raise ValueError("Specified directory couldn't be found.")
            if len(sys.argv) > 3:
                suffix = sys.argv[3] == "suffix"
                if len(sys.argv) > 4:
                    additive = sys.argv[4] == "additive"
        main(particle, filepath, suffix, additive)
    else:
        print('Usage: python prefixer-suffixer.py [particle] [directory] [prefix/suffix] [additive]\nExample usage: python prefixer-suffixer.py "Unwanted Suffix" "folder/nestedfolder" suffix')
