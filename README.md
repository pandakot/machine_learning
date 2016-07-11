First, run

```
python process_dataset.py --dataset your-dataset.csv --model-folder your-new-model

```

Replace params_len in train_nn.py with number of lines of dict.txt. 

Then execute 

```
python train_nn.py --model-folder your-new-model


python predict_nn.py "your phrase"
```
