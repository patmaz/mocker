from flask import Flask, request, jsonify
from faker import Faker
fake = Faker()

app=Flask(__name__)

def name():
    return fake.name()

def sentence():
    return fake.sentence()

def address():
    return fake.address()

def company():
    return fake.company()

def paragraph(nb_sentences=10):
    return fake.paragraph(nb_sentences=nb_sentences, variable_nb_sentences=False, ext_word_list=None)

fakers = {
    "name": name,
    "sentence": sentence,
    "address": address,
    "company": company,
    "paragraph": paragraph,
}

@app.route('/mock', methods=['POST'])
def root():
    dataJson=request.get_json(request.data)
    model=dataJson['model']
    number=dataJson['number']

    mockData=[]
    
    for i in range(0, number):
        item={}
        for key, value in dataJson['model'].items():
            if value in fakers:
                item[key]=fakers[value]()
            else:
                item[key]=fakers['sentence']()
        mockData.append(item)

    print(mockData)

    return jsonify(
        data=mockData
    ), 200

if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)