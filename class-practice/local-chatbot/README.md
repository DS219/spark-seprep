## Run a Local Chatbot

This assumes you have a model running and accessible at `http://localhost:8000`. To
check, you can run the following from your terminal:

```bash
curl localhost:8000/v1/models
```
This should output information about what model is being served.

### Start the Streamlit application

This assumes you are in this directory. If you already are in a virtual env, you 
can use that. If you are not, you can:

```bash
python3 -m venv venv-chatbot
source venv-chatbot/bin/activate
```

Install the required packages with 

```bash
pip3 install -r requirements.txt
```

You should now be able to run the Streamlit chatbot!

```bash
streamlit run chatbot.py
```

Access the chatbot application from your browser by navigating to `localhost:8501`

To exit a virtual environment, run:

```bash
deactivate
```

The venv-chatbot folder will still exist, so next time you want to run the chatbot:

```bash
cd class-practice/local-chatbot
source venv-chatbot/bin/activate
streamlit run chatbot.py
# Ctrl-C to exit program
```

Feel free to use any python package manager, you don't need to use venv. 
