[database]
- contains <Base> object for ModelType Table Reference to create Tables by Python and be used as a middleware datatype for <tableCreation> with ENGINE & <queryTransations> with SESSION


[session]
- contains <get_db> function to create sessions with the <SessionLocal> object for transactions between SQL and Python [will need support with DB Models and PyDantic Models]
- the <engine> object is not used because <alembic> manage the migrations to the <DB>


[models]    -> <datatype>:<db_models>
- contains Tables created with <Base> to be used as a <link> between SQL and Python


[schemas]   -> <datatype>:<pydantic_models>
- contains datatype to give support to @endpoints on the <request> input and <response> output DataType to be compatible with FastAPI operations
- Can be used on previus file of endpoints, like in 'service.py'


[service]
- contains <functions> to operate between SQL and Python with <db_models> and sometimes <pydantic_models> for datatype support


[routes]    ->  @endpoints
- contains <endpoints> for the REST-API