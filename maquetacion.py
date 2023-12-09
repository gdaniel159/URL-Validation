from tkinter import *
from tkinter import ttk
import requests
import json

class MainFrame(ttk.Frame):

    def __init__(self,container):
        
        super().__init__(container)
        self.container = container
        self.create_widget()

    def create_widget(self):

        self.font = ('Consola',12)
        self.url = StringVar(value='')

        self.label = ttk.Label(self.container,text="Ingrese URL: ",font=self.font).grid(row=0,column=0,padx=10,pady=10)
        self.entry = ttk.Entry(self.container,textvariable=self.url,font=self.font).grid(row=0,column=1,padx=10,pady=10)

        self.button = ttk.Button(self.container,text="Verificar",command=self.validar, width=50).grid(row=1,column=0, columnspan=2,padx=10,pady=10)

    def validar(self):

        self.API_KEY = "YOUR_API_KEY"
        
        url = "https://www.virustotal.com/api/v3/urls"

        payload = { "url": self.url.get() }
        headers = {
            "accept": "application/json",
            "x-apikey": self.API_KEY,
            "content-type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers)

        data = json.loads(response.text)

        analysis_id = data['data']['id']

        self.analysis_id = analysis_id

        self.validate_url()

    def validate_url(self):

        url = f"https://www.virustotal.com/api/v3/analyses/{self.analysis_id}"

        headers = {
            "accept": "application/json",
            "x-apikey": self.API_KEY
        }

        response = requests.get(url, headers=headers)

        data_validate = json.loads(response.text)

        print("URL Analizada: ", data_validate['meta']['url_info']['url'])
        print("Status: ", data_validate['data']['attributes']['status'])
        print("Stats: ", data_validate['data']['attributes']['stats'])