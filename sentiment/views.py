from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
import joblib

# بارگذاری مدل آموزش‌دیده
model = joblib.load('sentiment_model.pkl')

def analyze_sentiment(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            prediction = model.predict([msg.text])[0]
            msg.sentiment = prediction
            msg.save()
            return redirect('sentiment_result', msg.id)
    else:
        form = MessageForm()
    return render(request, 'sentiment/form.html', {'form': form})

def show_result(request, pk):
    msg = Message.objects.get(pk=pk)
    return render(request, 'sentiment/result.html', {'message': msg})
