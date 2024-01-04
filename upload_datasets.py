from datasets import load_dataset

dog_breed       = load_dataset("imagefolder", data_dir="./dog-breed-imagefolder-dataset",    drop_labels = False)

dog_breed       .push_to_hub("ajinkyakolhe112/dog_breed_classification")
