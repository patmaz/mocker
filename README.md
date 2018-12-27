# mocker app
##The app for generating mock data. 

To try it, send a POST request to the `https://mocker-app.herokuapp.com/mock` endpoint. The payload should contain a `number` of items that you want to generate and a `model` of each item (see fields available below).

```
{
	"number": 5,
	"model": {
		"name": "name",
		"text": "paragraph",
    	"sentence": "sentence",
    	"address": "address",
    	"company": "company"
	}
}
```