import rnn
import nottingham_util
# import urllib
# import zipfile 

# url = "www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
# urllib.urlretrieve(url, "dataset.zip")

# zip = zipfile.ZipFile(r'Nottingham.zip')
# zip.extractall('data')

nottingham_util.create_model()

rnn.train_model()