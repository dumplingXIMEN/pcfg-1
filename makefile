all:clean train parse

train:
	python3 train.py input.txt model.txt
parse:
	python3 parse.py model.txt output.txt
clean:
	rm -rf model.txt output.txt *.pyc __pycache__
