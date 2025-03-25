import pandas as pd

def getDataframeSize(players):
	df = pd.DataFrame(players)
	rows, columns = df.shape
	return rows, columns
