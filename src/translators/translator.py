from transformers import MarianTokenizer, MarianMTModel
import pandas as pd
from tqdm import tqdm

class Translator:
    """
    Traduit une colonne d'un DataFrame en utilisant un modèle HuggingFace.
    """
    def __init__(self, model_name: str):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate_text(self, text: str) -> str:
        """
        Traduit une seule phrase.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def translate(self, df: pd.DataFrame, column: str, new_column: str = "translation") -> pd.DataFrame:
        """
        Traduit une colonne entière du DataFrame.
        """
        tqdm.pandas(desc="Traduction")
        df[new_column] = df[column].progress_apply(self.translate_text)
        return df