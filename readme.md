Probabilistic Context-Free Grammar Parser
========
It is an implementation of Probabilistic Context-Free Grammar Parser.

###Usage

#### Training

	make train

It reads data from `input.txt` and generates the model file, `model.txt`.

#### Parsing

	make parse

It will find the most likely parse for the given sentence, and print hte inside and outside log probabilities for all spans and labels to `output.txt`.

#### Cleaning

	make clean

Remove all cache files and results.
