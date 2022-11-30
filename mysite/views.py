from django.shortcuts import render, redirect
import pickle5 as pickle


def inicio(request):
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    return render(request,"index.html",loaded_model)

def modelo(request):
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))