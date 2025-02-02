import sys
import os

# Añadir el directorio 'src' al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
print(sys.path)