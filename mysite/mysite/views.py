from django.shortcuts import render
from django.http import JsonResponse
import openai

openai.api_key = 'Your OpenAI API KEY'

def get_completion(prompt):
    print(prompt)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.5,
        )
        response_text = response.choices[0].message['content'].strip()
        print(response_text)
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing your request. Please try again later."

def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'index.html')
