import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga c0 y una lista separada por ','
    de los valores de la columna c5a y c5b (unidos por ':') de la
    tabla tbl2.tsv.
    """
    # Cargo tbl2
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    # Construyo la pareja "c5a:c5b" como texto
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    # Agrupo por c0 y junto en una única cadena, ordenada alfabéticamente
    resultado = (
        df.groupby("c0")["c5"]
          .apply(lambda vals: ",".join(sorted(vals)))
          .reset_index()
    )
    return resultado
