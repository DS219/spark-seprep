# Podman AI Lab or Local LLM application

## Run an LLM powered application locally

Follow the directions from the Podman AI Lab documentation to [start a chatbot recipe](https://podman-desktop.io/docs/ai-lab/start-recipe).
You can choose any recipe from the `Recipe Catalog`. Choose a smaller model to reduce the resources necessary to run.
The `Codegen` recipe will by default use a model from HuggingFace that was fine-tuned
for code generation. The `Audio to Text` is a good option because the model is smaller. It's recommended to choose one of these options.

### Options if Podman Desktop won't work for you

There are a few examples we've covered in class you can try if you can't get Podman AI Lab running. 

* Run an LLM locally and natively (no containers!) with llama.cpp server from class [example](https://github.com/DS219/spark-seprep/blob/main/class-practice/setup_local_llm.md).
  Then, pair this with a [local ChatBot](https://github.com/DS219/spark-seprep/tree/main/class-practice/local-chatbot) - consider modifying the chatbot.py script to make it your own.

* Run the RAG Chatbot with containers [example](https://github.com/DS219/spark-seprep/tree/main/class-practice/rag-chatbot-tutorial). Try with a different model if you've already run this. Test the RAG capabilities.

* The Podman AI Lab recipes repository holds the code from which you can run the applications natively (no containers). The READMEs should guide you. See [ai-lab-recipes repository](https://github.com/containers/ai-lab-recipes/tree/main/recipes)
  
## Present your application

For the assignment, each of you will show your model running with podman-desktop and the AI application
you chose. Why did you choose the application you chose? Did you try others? Did you try different models? Did it hallucinate?
Tell us anything interesting you encountered while running
the AI application. If you ran into issues, tell us about them! How did you fix them or try to fix them?

The presentation should be 1.5 minutes or less. Use an editor to include only the parts worth showing! We don't want to 
wait for your model or image to download on your video. Provide a link for your video in the form provided. 
**Form will be added to this page within the next few days**

In previous semesters, the `Audio to Text` application was a popular choice.
All the best and have fun! Extra credit for those that try out some interesting applications!
