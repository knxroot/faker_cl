#Faker CL

A provider extension for the [Faker-Factory](https://pypi.python.org/pypi/fake-factory) module. Faker CL is focus in Chile context.

###Example:

```python
from faker import Factory
fake = Factory.create('es_ES')
from faker_cl import ChileanPhone, ChileanRut

fake.add_provider(ChileanPhone)
fake.add_provider(ChileanRut)

print fake.cl_land_phone()
print fake.cl_mobile_phone()


print u"""Hi, my name is: {nombre}, mi chilean rut is {rut} and my mobile number is {tel} """.format(
	nombre=fake.name(),
	rut=fake.cl_rut(),
	tel=fake.cl_mobile_phone()
	)
```

