cd ..
python -m build
python -m twine upload --repository testpypi dist/*