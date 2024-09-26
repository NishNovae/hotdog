# src/hnh/util.py

def summary(filename: str, pred: dict):
    threshold = 0.9
    hotdog = pred[0]['score']

    if hotdog >= threshold:
        label = "hotdog"
    else:
        label = "not hotdog"
    return { 
        "file": filename, 
        "hotdog-percent-chance": str(round(hotdog*100, 2)) + "%",
        "current threshold": str(round(threshold*100, 2)) + "%",
        "label": label
    }
