import openai
from IPython.display import Image
from IPython.core.display import HTML
from IPython.display import Image
from IPython.core.display import HTML 
from IPython import display
 
# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
#prompt = str(input("Enter your story prompt please: "))
def chatgpt(prompt):
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    res = completion.choices[0].text
    print(res)
    
    promptfortitle = "Give me a title for this story " + res
    completion0 = openai.Completion.create(
        engine=model_engine,
        prompt=promptfortitle,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    title = completion0.choices[0].text
    print(title)

    promptforpictures = "Give me 5 unique lines to search for pictures for this story " + res
    completion1 = openai.Completion.create(
        engine=model_engine,
        prompt=promptforpictures,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    keywords = completion1.choices[0].text
    print(keywords)



    listofkey = keywords.split("\n")
    final_keywords = []
    for i in listofkey:
        if len(i) > 0:
            j = i.split(".")
            final_keywords.append(j[1])
    urls_for_pics=[]
    for a in final_keywords:      
        response = openai.Image.create(
        prompt="a picture of "+ a + " for kids",
        n=1,
        size="1024x1024"
        )
        urls_for_pics.append(response['data'][0]['url'])
    #print(urls_for_pics)
    """for i in urls_for_pics:
        print(i)
        print(1)
        display.Image(url= i,width=400, height=400)"""
    return [res,urls_for_pics,title]
    
