# challenge 1
build an AI app in 2 days

## build instructions
### deploy model
run notebook.ipynb on google colab and save the model locally to the model
directory. then run `docker-compose up`

### run svelte app
```
cd app
npm ci
npm run start
```

### run proxy server
because we can't run opencv on js atm, the front end sends the file to a proxy
first, which then converts the image into a suitable format for the model.
```
cd proxy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

