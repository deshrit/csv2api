## csv2api

An example of creating secure, authenticated and request throttled
RESTful endpoints that  directly uploads data from csv file to database
and also access it from the endpoints.

A fixed schema of the model used in this case:

```python
class Animal(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    scientific_name = models.CharField(max_length=254)
    owner_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    contact = models.CharField(max_length=12)
    address = models.TextField()
```

Hitting `/api/csv` with payload csv file with name `file` example:

```
unique_id,name,scientific_name,gender,dob,owner_name,contact,address
1,"Goose, knob-nosed",Sarkidornis melanotos,Female,2022-12-18,Terra Dorbon,440-474-5623,60609 Glacier Hill Road
2,Cape cobra,Naja nivea,Female,2023-07-06,Otha Byram,300-641-8682,0188 Comanche Terrace
3,"Crow, pied",Corvus albus,Female,2022-08-15,Carly Flori,582-436-7280,2408 Talmadge Way
4,"Curlew, black",Haematopus ater,Male,2023-03-06,Kimbell Boatwright,897-612-0476,83 Messerschmidt Terrace
```

## Live

[live](https://csvtoapi.pythonanywhere.com/api/swagger-ui)

## Documentation

[docs](https://csvtoapi.pythonanywhere.com/api/docs)
