import os
from textsummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from textsummarizer.entity import DataTransformationconfig


class DataTransformation:
    def __init__(self,config:DataTransformationconfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encoding = self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(example_batch['summary'],max_length=128,truncation=True)

            return {
                "input_ids" : input_encoding['input_ids'],
                "attention_mask": input_encoding["attention_mask"],
                "labels" : target_encoding['input_ids']
            }
        
    def convert(self):
        datasets = load_from_disk(self.config.data_path)
        datasets_pt = datasets.map(self.convert_examples_to_features,batched=True)
        datasets_pt.save_to_disk(os.path.join(self.config.root_dir,"dataset"))