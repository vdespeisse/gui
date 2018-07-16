import os

BASE_PATH = os.path.join(os.path.dirname(__file__),'..')
PATH_DATA = os.path.join(BASE_PATH, 'data')

def run(filepath, model='basic', multiplier=1):
  data = open(os.path.join(PATH_DATA,filepath)).read()
  result = compute(data,model,float(multiplier))

  return {
    'result': result,
    'filename': filepath,
    }

def compute(data, model,multiplier):
  return len(data)*multiplier
