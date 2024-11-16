import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report
from transformers import AutoTokenizer, AutoModel
import torch
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")

class Pipeline:
    def __init__(self, model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2', weights="samaya_pizdataya_model"):
        self.ml_model = CatBoostClassifier()     
        self.ml_model.load_model(weights)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def read_data(self, file_path, sep="\t", header=None, batch_size=32):
        def change_delimiter(val):
            val = list(val)
            val[-3] = "."
            return "".join(val)

        self.df = pd.read_csv(file_path, sep=sep, header=None)
        if len(self.df.columns) != 4:
            raise Exception("Неверное кол-во колонок")
            
        self.df.columns = ["id", "date", "summ", "description"]
        self.df.summ = self.df.summ.apply(change_delimiter)
        self.df.date = pd.to_datetime(self.df.date, format='%d.%m.%Y')
        self.df['clean_description'] = self.df['description'].str.lower()
        self.df['clean_description'] = self.df['description'].str.lower()
        
        X_text_unlabeled = self.get_text_embeddings(self.df['clean_description'].tolist(), batch_size=batch_size)
        self.X_unlabeled = pd.concat(
            [pd.DataFrame(X_text_unlabeled), self.df[['summ']]], axis=1
        )
    def get_text_embeddings(self, texts, batch_size=32):
        embeddings = []
        self.model.eval()
        with torch.no_grad():
            for i in tqdm(range(0, len(texts), batch_size)):
                batch_texts = texts[i:i + batch_size]
                encoded = self.tokenizer(batch_texts, padding=True, truncation=True, return_tensors="pt")
                output = self.model(**{k: v.to(self.model.device) for k, v in encoded.items()})
                embeddings.append(output.pooler_output.cpu())
        return torch.cat(embeddings).numpy()

    def predict(self, data_path, sep="\t", header=None, out_file_name="output.csv", batch_size=32):
        self.read_data(data_path, sep, header, batch_size=batch_size)
        self.df["target"] = self.ml_model.predict(self.X_unlabeled).flatten()
        self.df[["id", "target"]].to_csv(out_file_name, index=False)

pipeline = Pipeline()
pipeline.predict("payments_main.tsv", batch_size=64)
