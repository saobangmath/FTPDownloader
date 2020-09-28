import urllib.request as req

url = "ftp://parrot.genomics.cn/gigadb/pub/10.5524/100001_101000/100627/assemblies/"
target_path = "-translated-protein.fa.gz"
dest_path = "C://Users/v/Desktop/Biology/" # thay bang cai link den cai folder em muon luu cai dong files kia vao

with req.urlopen(url)as resp:
      dirs = resp.read().decode('utf-8').split()
      for i in range(8, len(dirs), 9):
          prefix = dirs[i][:4:]
          if prefix != "LHLE": # file LHLE could not be installed (505 error)
              source = url + dirs[i] + "/" + prefix + target_path
              dest = dest_path + prefix[0] + "/" + prefix + target_path
              req.urlretrieve(source, dest)
              print("File: "+prefix + target_path + " is downloaded!")
print("Done!")
