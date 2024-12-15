import pickel
pickel.dump(svc, open("ml_model.pkl","wb"))
pickel.dump(finetuned model,open("file_name" , "mode"))
--> To load the file..
pickel.load(open("ml_model.pkl","rb"))
