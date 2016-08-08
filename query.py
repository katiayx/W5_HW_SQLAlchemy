"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all() #didn't work like this: Model.query.filter_by(year < 1960).all() 
#error message says 'name 'year' is not defined' -- don't understand why

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all() #keep getting TypeError: %d format: a number is required, not NoneType. I checked and 
#checked again my model.py's __repr__ method, and my schema, and I can't find where the 
#error is.

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded==1903)&(Brand.discontinued == None)).all() #still 
#getting TypeError: %d format: a number is required, not NoneType. But I think the query is right. 

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued != None)|(Brand.founded < 1950)).all() #query feels right, 
#but still the same error as before

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    mods = db.session.query(Model.year,
                            Model.name,
                            Model.brand_name,
                            Brand.headquarters).join(Brand).all()

    for mod in mods:
        if Model.year == year:
            print Model.name, Model.brand_name, Brand.headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
 
    each_brand = db.session.query(Brand.name,
                            Model.name).join(Model).all()

    for name, name in each_brand:
        print name, name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
"""It's an object of the SQLAlchemy query class"""

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
"""I think of the association table as a connector tables that have a many-to-many relationship.
Association table does not contain any meaningful data, so user would never search for something
in the Association table. Assoication table is used to connect many-to-many tables"""

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """returns a list of objects that are brands whose name contains or is 
    equal to the input string"""

    Brand.query.filter(Brand.name==mystr).all()


def get_models_between(start_year, end_year):
    """returns a list of objects that are models with years that fall between 
    the start year (inclusive) and end year (exclusive)"""


    Model.query.filter((start_year=<Model.year)&(Model.year<=end_year).all()
    
