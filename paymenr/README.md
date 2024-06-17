pip install sqlalchemy

pip install nltk


poetry add pyjwt


The psycopg2-binary package is a stand-alone package that includes the binary for the psycopg2 package and does not require you to have PostgreSQL installed on your machine to compile it.
pip install psycopg2-binary


Install psycopg2
Psycopg2 is a popular python library for running raw Postgres queries.

For most operating systems, the quickest installation method is using the PIP package manager. For example:
# pip install psycopg2-binary


from starlette.config import Config
from starlette.datastructures import Secret 

load_dotenv()



try:
    config = Config(".env")
except FileNotFoundError:
        config = Config()


ITEM_NAME = config("ITEM_NAME")



passlib.context is a module from the Passlib library, which is a password hashing library for Python. It provides a variety of hashing algorithms and utilities to work with password hashes.

Here’s an explanation of your code:

CryptContext This is a class from Passlib that provides a context for cryptographic hashing schemes. It allows you to define a set of hash algorithms (schemes) and various policies related to them.




# pip install passlib
