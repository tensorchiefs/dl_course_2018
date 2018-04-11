import os.path, time, os

COLAB = 'https://colab.research.google.com/github/'
REPNAME = 'tensorchiefs/dl_course_2018/blob/master/notebooks/'
PREFIX_COLAB = COLAB + REPNAME
PREFIX_GITUB = 'https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/'

if __name__ == '__main__':
    files = os.listdir()
    notebooks = [f for f in  files if f.endswith('ipynb')]
    for nb in sorted(notebooks):
        print("* " + nb + " [Colab]" + "(" + PREFIX_COLAB + nb + ")" + " [github]" + "(" + PREFIX_GITUB + nb + ")")
    print('\n list created with create_notebooks_overview.py')
