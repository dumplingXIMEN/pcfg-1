Probabilistic Context-Free Grammar Parser
========
It is an implementation of Probabilistic Context-Free Grammar Parser.

###Usage

#### Training

	$ make train

It reads data from `input.txt` and generates the model file, `model.txt`.

```
$ cat input.txt
(S(NP(DT The)(NN boy))(VP(VP(VBD saw)(NP(DT a)(NN girl)))(PP(IN with)(NP(DT a)(NN telescope)))))
(S(NP(DT The)(NN girl))(VP(VBD saw)(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope))))))

$ cat model.txt
PP # IN NP # 1.0
VP # VBD NP # 0.6666666666666666
VP # VP PP # 0.3333333333333333
NP # DT NN # 0.8571428571428571
NP # NP PP # 0.14285714285714285
NN # boy # 0.3333333333333333
NN # telescope # 0.3333333333333333
NN # girl # 0.3333333333333333
DT # a # 0.6666666666666666
DT # the # 0.3333333333333333
S # NP VP # 1.0
VBD # saw # 1.0
IN # with # 1.0
```

#### Parsing

	$ make parse

It will find the most likely parse for the given sentence, and print hte inside and outside log probabilities for all spans and labels to `output.txt`.

```
$ cat output.txt
(S(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope))))(VP(VBD saw)(NP(DT a)(NN girl))))
0.0006581619798335054
DT # 1 # 1 # 0.6666666666666666 # 0.0009872429697502581
DT # 4 # 4 # 0.6666666666666666 # 0.0009872429697502581
DT # 7 # 7 # 0.6666666666666666 # 0.0009872429697502581
IN # 3 # 3 # 1.0 # 0.0006581619798335054
NN # 2 # 2 # 0.3333333333333333 # 0.0019744859395005162
NN # 5 # 5 # 0.3333333333333333 # 0.0019744859395005162
NN # 8 # 8 # 0.3333333333333333 # 0.0019744859395005162
NP # 1 # 2 # 0.19047619047619047 # 0.0034553503941259036
NP # 1 # 5 # 0.005183025591188856 # 0.12698412698412698
NP # 4 # 5 # 0.19047619047619047 # 0.0034553503941259036
NP # 7 # 8 # 0.19047619047619047 # 0.0034553503941259036
PP # 3 # 5 # 0.19047619047619047 # 0.0034553503941259036
S # 1 # 8 # 0.0006581619798335054 # 1.0
VBD # 6 # 6 # 1.0 # 0.0006581619798335054
VP # 6 # 8 # 0.12698412698412698 # 0.005183025591188856
```

#### Cleaning

	make clean

Remove all cache files and results.
